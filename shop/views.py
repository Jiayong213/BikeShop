from django.views import View
from .models import Bike, Order, Basket
from django.views.generic import ListView,DetailView
from .forms import BikeOrderForm
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.db import transaction


@transaction.atomic
def update_bike_parts(bike):
    bike.frame.quantity -= 1
    bike.frame.save()
    bike.seat.quantity -= 1
    bike.seat.save()
    bike.tire.quantity -= 2
    bike.tire.save()
    if bike.has_basket:
        basket = Basket.object.first()
        if basket and basket.quantity > 0:
            basket.quantity -= 1
            basket.save()


class BikeList(ListView):
    model = Bike
    template_name = 'bike_list.html'

class BikeDetail(DetailView):
    model = Bike
    template_name = 'bike_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form'] = BikeOrderForm()
        return context
    
    def post(self, request, *args, **kwargs):
        form = BikeOrderForm(request.POST)
        self.object = self.get_object()
        if form.is_valid():
            order = Order.objects.create(
                bike = self.object,
                status = 'pending',
                name = form.cleaned_data['name'],
                surname = form.cleaned_data['surname'],
                phone_number = form.cleaned_data['phone_number'],
            )
            update_bike_parts(self.object)
            return redirect(reverse('order_success', kwargs={'order_id': order.id}))
        return render(request, self.template_name, {'form': form, 'object': self.object})
    
def order_success(request, order_id):
    order = get_object_or_404(Order, id = order_id)
    return render(request, 'shop/order_success.html', {'order': order})
