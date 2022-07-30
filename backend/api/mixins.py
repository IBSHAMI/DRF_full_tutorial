from rest_framework import permissions
from .permissions import IsStaffProductEditPermission

class StaffEditorPermissionMixin(): 
    permission_classes = [permissions.IsAdminUser, IsStaffProductEditPermission]