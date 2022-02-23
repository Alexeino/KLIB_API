from rest_framework import permissions

class ReviewOwnerOrReadOnly(permissions.BasePermission):
    
    def has_object_permission(self,request,view,obj):
        if request.user.is_anonymous:
            return False
        return (request.method in permissions.SAFE_METHODS 
        or obj.review_user == request.user)
    
        
class IsAdminOrReadOnly(permissions.BasePermission):
    
    def has_permission(self,request,view):
        
        return (request.method in permissions.SAFE_METHODS 
                or request.user.is_staff) 