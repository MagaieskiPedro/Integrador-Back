from rest_framework.permissions import BasePermission

class isAdmin(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.categoria == 'A':
            return True
        return False
class isComum(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated and request.user.categoria == 'C':
            return True
        return False
class isAuthenticated(BasePermission):
    def has_permission(self, request, view):
        if request.user.is_authenticated:
            return True
        return False