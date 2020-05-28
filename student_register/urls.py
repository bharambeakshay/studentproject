from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.student_form, name = "student_insert"),#localhost , get and podt for insert operation
    path('<int:id>/',views.student_form, name = "student_update"), # get and podt for update operation
    path('<int:id>/',views.student_delete, name = "student_delete"), #for deleting the employee
    path('list/',views.student_list) #To retrieve and display all records 
]
