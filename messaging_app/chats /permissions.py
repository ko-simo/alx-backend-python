# permissions.py

from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow users to access their own objects.
    """

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
