from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveDestroyAPIView
)
from rest_framework.permissions import IsAuthenticated

from .models import TransactionHistory

from .serializers import TransactionHistorySerializer

from .permissions import (
    PossibleToCreateTransactionHistory, 
    PossibleToDeleteTransactionHistory
)


class TransactionHistoryCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated, PossibleToCreateTransactionHistory]
    serializer_class = TransactionHistorySerializer


class TransactionHistoryListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = TransactionHistorySerializer

    def get_queryset(self):
        return TransactionHistory.objects.filter(store__user=self.request.user)


class TransactionHistoryDetailView(RetrieveDestroyAPIView):
    queryset = TransactionHistory.objects.all()
    serializer_class = TransactionHistorySerializer
    permission_classes = [IsAuthenticated, PossibleToDeleteTransactionHistory]