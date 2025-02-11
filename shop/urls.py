from django.urls import path
from . import views

urlpatterns = [
    path('bikes/',views.BikeList.as_view(), name='bike_list'),
    path('bikes/<int:pk>', views.BikeDetail.as_view(), name='bike_detail'),
    path('order/<int:order_id>/', views.order_success, name='order_success'),

]