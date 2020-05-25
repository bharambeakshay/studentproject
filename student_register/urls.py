
from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.studentform),#localhost
    path('list/',views.student_list)
]
