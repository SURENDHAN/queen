from django.urls import path
from . import views

urlpatterns = [
    path('', views.nqueens_view, name='nqueens_view'),
]
