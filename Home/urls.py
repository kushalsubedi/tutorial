
from django.urls import path  

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path ('add/',views.add_student,name ='add'),
    path ('info/<int:id>/',views.retrive_student, name ='info'),
    path ('update/<int:id>/',views.update_student, name ='update'),
    path ('delete/<int:id>/',views.delete_student, name ='delete')
]
