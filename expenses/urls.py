from django.urls import path
from . import views
from theme.views import index

urlpatterns = [
    path("index/",index,name="index"),
    path("expenses/", views.expenses, name="expenses"),
    path("updateExpense/", views.updateExpense, name="updateExpense"),


    # api path
    path("api/deleteExpense/", views.deleteExpense, name="deleteExpense"),
    path("api/searchByExpenseDate/", views.searchByExpenseDate, name="searchByExpenseDate"),
    path("api/searchByExpenseHeadOfAccount/", views.searchByExpenseHeadOfAccount, name="searchByExpenseHeadOfAccount"),
    path("api/searchByExpenseData/", views.searchByExpenseData, name="searchByExpenseData"),
    # path("api/searchbyname/", views.searchbyname, name="searchbyname"),
]