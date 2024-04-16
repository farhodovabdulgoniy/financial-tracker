from rest_framework.permissions import BasePermission


class IsOwnerOfStore(BasePermission):
    def has_object_permission(self, request, view, obj):
        """
        !works only for existing objects
        """
        return obj.user == request.user
