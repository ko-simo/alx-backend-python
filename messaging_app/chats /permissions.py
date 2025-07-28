from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Only allows users to access their own messages/conversations.
    """

    def has_object_permission(self, request, view, obj):
        return obj.user == request.user
