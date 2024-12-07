
from django.urls import path
from . import views


urlpatterns = [
    path("",                                views.allemployees, name="allemployees"),
    path("allemployees/",                   views.allemployees, name="allemployees"),
    path("singleemployee/<int:empid>/",     views.singleemployee, name="singleemployee"),
    path("schedulingemployee/",             views.schedulingemployee, name="schedulingemployee"),
    path("addemployee/",                    views.addemployee, name="addemployee"),
    path("attendance/",                     views.attendance, name="attendance"),
    path("deleteemployee/<int:empid>/",     views.deleteemployee, name="deleteemployee"),
    path("updateemployee/<int:empid>/",     views.updateemployee, name="updateemployee"),
    path("doupdateemployee/<int:empid>/",     views.doupdateemployee, name="doupdateemployee"),
    path("employeescheduled/",             views.employeescheduled, name="employeescheduled"),
    path("deleteschedule/<int:empid>/",     views.deleteschedule, name="deleteschedule"),

]