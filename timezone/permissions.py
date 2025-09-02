from rest_framework.permissions import BasePermission

class IsOwnerOrAdmin(BasePermission):
    """
    Only the owner of the timezone entry can edit/delete.
    Admin and Manager can access all entries.
    """

    def has_object_permission(self, request, view, obj):
        if request.user.role in ['admin', 'manager']:
            return True
        return obj.user == request.user
