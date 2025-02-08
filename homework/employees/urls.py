from .views import ListCreateApiView, RetriveUpdateDestroyApiView
from django.urls import path

urlpatterns = [
    path('employees/', ListCreateApiView.as_view(), name='ListCreateApiView'),
    path('employees/<int:pk>/', RetriveUpdateDestroyApiView.as_view(), name='RetriveUpdateDestroyApiView'),
]
