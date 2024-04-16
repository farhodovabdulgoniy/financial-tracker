from django.urls import path

from .views import (
    TransactionHistoryCreateView,
    TransactionHistoryListView,
    TransactionHistoryDetailView,
)


urlpatterns = [
    path('', TransactionHistoryListView.as_view()),
    path('<int:pk>/', TransactionHistoryDetailView.as_view()),
    path('create/', TransactionHistoryCreateView.as_view()),
]
