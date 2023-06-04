from rest_framework import permissions
from .permissions import IsStaffEditorPermssion


class StaffEditorPermissionMixin():
    permission_class=[permissions.IsAdminUser, IsStaffEditorPermssion]


