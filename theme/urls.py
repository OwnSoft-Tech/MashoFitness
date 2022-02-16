from django.urls import path
from django.contrib import admin
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('addMember/', views.addMember, name='addMember'),
    path('addTeam/', views.addTeam, name='addTeam'),
    path("bodyAssesments/", views.bodyAssesments, name="bodyAssesments"),
    path("createUser/", views.createUser, name="createUser"),
    path("employee/", views.employee, name="employee"),
    path("futsal", views.futsal, name="futsal"),
    path("futsalMatch/", views.futsalMatch, name="futsalMatch"),
    path("gymManagement", views.gymManagement, name="gymManagement"),
    path("GymSetting/gymSetting/", views.gymSetting, name="gymSetting"),
    path("GymSetting/editGymSetting/", views.editGymSetting, name="editGymSetting"),
    path("login/", views.login, name="login"),
    path("memberDetails/", views.memberDetails, name="memberDetails"),
    path("printform/", views.printform, name="printform"),
    path("smshistory/", views.smshistory, name="smshistory"),
    path("teamDetails/", views.teamDetails, name="teamDetails"),
    path("viewMembers/", views.viewMembers, name="viewMembers"),
    path("viewRecord/", views.viewRecord, name="viewRecord"),
    path("viewTeam/", views.viewTeam, name="viewTeam"),
    path("matches/", views.matches, name="matches"),
    path("updateFutsalMatch/", views.updateFutsalMatch, name="updateFutsalMatch"),




    # """
    # API path for the ajex call
    # """
    path("api/get_membershipCategory/", views.get_membershipCategory, name="api_get_membershipCategory"),
    path("api/deleteMember/", views.deleteMember, name="deleteMember"),
    path("api/searchbydata/", views.searchbydata, name="searchbydata"),
    path("api/searchbydate/", views.searchbydate, name="searchbydate"),
    path("api/searchbyname/", views.searchbyname, name="searchbyname"),
    # path("delete_record/", views.delete_record, name="delete_record"),

    # ex: /polls/
    # path('', views.home, name='home'),
    # path('login', views.login, name='login'),
    # path('signup', views.signup, name='signup'),
    # path('order', views.order, name='order'),
    # path("logout", views.logout, name= "logout"),
    # path('order_details',views.order_details, name='order_details'),
    # path('user_details',views.user_details, name='user_details'),
    # path('admin:index/', admin.site.urls, name='admin'),
    # path('order', views.update, name='update'),

    # path('categories/', views.CategoryView.as_view(), name='categories'),
    # path('BookingCategories/<int:pk>', views.CategoryDetailView.as_view(), name='category-detail')
]