from rest_framework.generics import (
    ListAPIView,
    RetrieveUpdateDestroyAPIView,
    CreateAPIView
)
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

from .models import Store

from .serializers import (
    StoreSerializer,
    StoreUpdateSerializer
)

from .permissions import IsOwnerOfStore


class StoreCreateView(CreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = StoreSerializer

    def post(self, request):
        serializer = self.serializer_class(data=request.data)

        if serializer.is_valid():
            serializer.save(user=request.user)
            return Response(serializer.data)

        return Response(serializer.errors, status=400)


class StoreListView(ListAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = StoreSerializer

    def get_queryset(self):
        return Store.objects.filter(user=self.request.user)


class StoreDetailView(RetrieveUpdateDestroyAPIView):
    serializer_class = StoreUpdateSerializer
    permission_classes = [IsAuthenticated, IsOwnerOfStore]
    queryset = Store.objects.all()
