from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from bankingapp import views

urlpatterns = [
    path('index/', views.Homepage.as_view(), name="homepage"),
    path('view_all_customers/', views.ViewAllCustomers.as_view(), name="view_all_customers"),
    path('customer_detail/<pk>/', views.CustomerDetail.as_view(), name="customer_detail"),
    path('transfer_money/<pk>/', views.TransferMoney.as_view(), name="transfer_money"),
]
