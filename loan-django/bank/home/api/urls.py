from django.urls import path, include
from . import views 
from rest_framework import routers

router = routers.DefaultRouter()




urlpatterns = [
    path('', views.login,name='login'),
    path('customer/request_loan/', views.RequestLoan.as_view()),   #customer request loan with amount from bank (takes customerID , amount )
    path('provider/add_fund/', views.AddFund.as_view()),
    path('provider/create_fund/', views.CreateFund.as_view()),
    path('provider/view_fund/', views.ViewFund.as_view()),
    path('banker/loan_requests/', views.LoansView.as_view()),

]

