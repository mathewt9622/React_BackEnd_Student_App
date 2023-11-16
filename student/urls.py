from django.urls import path,include

from . import views


urlpatterns = [
    path('viewall/', views.viewAll,name="viewAll"),
    path('add/', views.add,name="add"),
    
]
