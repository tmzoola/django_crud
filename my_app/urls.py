from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('', views.home, name='home'),
    path('add/', views.add, name='add'),
    path('delete/<int:id>', views.delete ),
    path('update/<int:id>', views.update ),
    path('update_new/<int:id>', views.update_new ),
]