from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.student_form),#localhost
    path('list/',views.student_list)
]
