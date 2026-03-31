"""
Permission classes for API authentication.
Validates JWT tokens from Authorization header.
"""
from rest_framework.permissions import BasePermission


class IsAdminAuthenticated(BasePermission):
    """
    Permission class that requires a valid JWT token in the Authorization header
    and that the user is an admin/staff.
    """
    message = "Authentication required. Please provide a valid token."

    def has_permission(self, request, view):
        # Token validation is done by JWT authentication
        # This checks that user is authenticated and is staff
        if request.user and request.user.is_authenticated:
            return request.user.is_staff
        return False
