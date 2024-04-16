from django.urls import path

from .views import (
    StoreListView,
    StoreDetailView,
    StoreCreateView
)

urlpatterns = [
    path('', StoreListView.as_view()),
    path('<int:pk>/', StoreDetailView.as_view()),
    path('create/', StoreCreateView.as_view()),
]