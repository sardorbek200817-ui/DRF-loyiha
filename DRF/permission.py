from rest_framework.permissions import BasePermission


class IsOwnr(BasePermission): 
    def has_object_permission(self, request, view, obj):
        return obj.owner == request.user

class IsManager(BasePermission):

    def has_object_permission(self, request, view, obj):
        return obj.user.status == "Manager"
