# timezone/permissions.py
from rest_framework.permissions import BasePermission, SAFE_METHODS

class IsOwnerOrAdmin(BasePermission):
    """
    Custom permission: Only allow owners or admins to edit objects.
    """

    def has_object_permission(self, request, view, obj):
        # Read permissions are allowed to any request
        if request.method in SAFE_METHODS:
            return True

        # Write permissions only for admin or object owner
        return request.user.role in ['admin', 'manager'] or obj.user == request.user
