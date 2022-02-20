from rest_framework import permissions

class ReviewOwnerOrReadOnly(permissions.BasePermission):
    
    def has_object_permission(self,request,view,obj):
        return (
            request.method in permissions.SAFE_METHODS
            or obj.review_user == request.user
        )