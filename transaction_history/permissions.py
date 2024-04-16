from rest_framework.permissions import BasePermission

from store.models import Store


class PossibleToCreateTransactionHistory(BasePermission):
    def has_permission(self, request, view):
        store_id = request.data.get('store', None)
        if store_id:
            try:
                store = Store.objects.get(id=store_id)
            except store.DoesNotExist:
                return False
            return store.user == request.user
        return False
    

class PossibleToDeleteTransactionHistory(BasePermission):
    def has_object_permission(self, request, view, obj):
        return obj.store.user == request.user