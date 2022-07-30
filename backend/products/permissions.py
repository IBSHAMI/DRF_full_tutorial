import re
from rest_framework import permissions

# by deaf


class IsStaffProductEditPermission(permissions.DjangoModelPermissions):
    # GET, HEAD, OPTIONS = SAFE_METHODS that user can access even without permission
    # we can overwrite the has_permission method to handle the unsafe methods
    perms_map = {
        'GET': ['%(app_label)s.view_%(model_name)s'], # for list and detail
        'OPTIONS': [],
        'HEAD': [],
        'POST': ['%(app_label)s.add_%(model_name)s'],
        'PUT': ['%(app_label)s.change_%(model_name)s'],
        'PATCH': ['%(app_label)s.change_%(model_name)s'],
        'DELETE': ['%(app_label)s.delete_%(model_name)s'],
    }
    
    # def has_permission(self, request, view):
    #     user = request.user         
    #     # check if he is a staff
    #     if not request.user.is_staff:
    #         return False
        # return super().has_permission(request, view) # return default permission
        
    

    # --------- it will return True if only one of the conditions are met which is wrong --------
    # def has_permission(self, request, view):
    #     print(request.user)
    #     # check if user is --something
    #     # check if he has premission to do anything to specific model
    #     # has_prem('app_name.action_name_model_name')
    #     if request.user.is_staff:
    #         print(request.user.get_all_permissions())
    #         if request.user.has_perm('products.view_product'): # "app_name.action_model_name"
    #             return True
    #         if request.user.has_perm('products.edit_product'):
    #             return True
    #         if request.user.has_perm('products.delete_product'):
    #             return True
    #         if request.user.has_perm('products.add_product'):
    #             return True
    #         return False
    #     return False
