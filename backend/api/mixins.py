from rest_framework import permissions

from .permissions import IsStaffEditor


# I can now use this custom mixin in any view
class StaffEditorMixin(object):
    permission_classes = [permissions.IsAdminUser, IsStaffEditor]
