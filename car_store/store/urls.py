from django.urls import path
from car_store.store.views import StoreView, CarView

urlpatterns = [
    path('stores/', StoreView.as_view()),
    path('stores/<int:pk>/', StoreView.as_view()),
    path('cars/', CarView.as_view()),
    path('cars/<int:pk>/', CarView.as_view()),
]
