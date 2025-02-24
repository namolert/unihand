from django.core.exceptions import PermissionDenied

def is_student(user):
    if not user.is_authenticated or user.role != "Student":
        raise PermissionDenied("You are not allowed to access this page.")
    
def is_professor(user):
    if not user.is_authenticated or user.role != "Professor":
        raise PermissionDenied("You are not allowed to access this page.")
    
def is_admin(user):
    if not user.is_authenticated or user.role != "Admin":
        raise PermissionDenied("You are not allowed to access this page.")