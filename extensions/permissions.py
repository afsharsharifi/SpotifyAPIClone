from rest_framework.permissions import BasePermission


class IsAdminOnlyPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.is_authenticated and request.user.is_admin


class AloowAllGetAdminPostPutDeletePermission(BasePermission):
    def has_permission(self, request, view):
        if request.method == "GET":
            return True
        elif request.method in ["POST", "PUT", "DELETE"]:
            return request.user.is_authenticated and request.user.is_admin
        return False


class UserGetAdminPostPutDeletePermission(BasePermission):
    def has_permission(self, request, view):
        if request.method == "GET":
            return request.user.is_authenticated
        elif request.method in ["POST", "PUT", "DELETE"]:
            return request.user.is_authenticated and request.user.is_admin
        return False
