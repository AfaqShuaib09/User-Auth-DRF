''' Custom Permissions for the User Api'''
from rest_framework import permissions


class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to make changes to it. (PUT, PATCH, DELETE)
    """

    def has_object_permission(self, request, view, obj):
        """
        Checks if the user has the permission.
        """
        return obj.user == request.user or request.method in permissions.SAFE_METHODS
