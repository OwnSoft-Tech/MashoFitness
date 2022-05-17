from django.urls import path
from . import views
from employees.views import index

urlpatterns = [
    path('index/', index, name='index'),
    path("customer/", views.customer, name="customer"),
    path("updateCustomer/", views.updateCustomer, name="updateCustomer"),
    

    # api path
]