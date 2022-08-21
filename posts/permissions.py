from rest_framework import permissions

class IsAuthOrReadOnly(permissions.BasePermission):
    def has_permission(self, request, view):
        #authenticatedusers can see list view
        if request.user.is_authenticated:
            return True
        return False

    def has_object_permission(self, request, view, obj):
#read permision all allowed GET HEAD or OPTIONS

        if request.method in permissions.SAFE_METHODS:
            return True
#write permission allowed to author of post
        return obj.author == request.user