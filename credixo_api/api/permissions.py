from rest_framework import permissions
from django.contrib.auth.models import Group

"""
A simple function to check whether the user has valid user group specified.
"""

def _is_in_group(user, group_name):
    """
    Takes a user and a group name, and returns `True` if the user is in that group.
    """
    try:
        return Group.objects.get(name=group_name).user_set.filter(id=user.id).exists()
    except Group.DoesNotExist:
        return None

def _has_group_permission(user, required_groups):
    return any([_is_in_group(user, group_name) for group_name in required_groups])

"""
CreatePermission restricts the Teacher from Creating the Super-Admin or Teacher and the Student from creating Any Users.
"""
class CreatePermission(permissions.BasePermission):
    
    def has_permission(self, request, view):
        # print(request.data['profile'])
        print('has_permission')
        print(request.data['profile']['group'])
        if _is_in_group(request.user,'Super-admin'):
            return True
        if _is_in_group(request.user,'Teacher') and request.data['profile']['group']==3:
            return True
        if _is_in_group(request.user,'Student'):
            return False
        return False
"""
List Permission Restricts the Students to view the list.
"""
class ListPermission(permissions.BasePermission):
    def has_permission(self, request, view):
        # print(request.data['profile'])
        print('ListPermission')
        if _is_in_group(request.user,'Super-admin'):
            return True
        if _is_in_group(request.user,'Teacher'):
            return True
        if _is_in_group(request.user,'Student'):
            return False
        return False
"""
DeletePermission restricts the Teacher to delete the Super-Admin or Teacher
"""
class DeletePermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # print(request.data['profile'])
        print('has_object_permission')
        print(_is_in_group(obj,'Student'))
        if _is_in_group(request.user,'Super-admin'):
            return True
        if _is_in_group(request.user,'Teacher') and (_is_in_group(obj,'Student')):
            return True
        if _is_in_group(request.user,'Student'):
            return False
        return False
"""
RetrievePermission is used to restrict Teacher from viewing the Other Teachers and allows Students to view their 
Object.
"""
class RetrievePermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # print(request.data['profile'])
        print('RetrievePermission')
        # print(_is_in_group(obj,'Student'))
        if _is_in_group(request.user,'Super-admin'):
            return True
        if _is_in_group(request.user,'Teacher'):
            if (_is_in_group(obj,'Student')):
                return True
            return obj==request.user
        if _is_in_group(request.user,'Student'):
            return obj==request.user
        return False
"""
UpdatePermission allows the Teacher to edit his or student's data, allows the student to edit his data.
"""
class UpdatePermission(permissions.BasePermission):
    def has_object_permission(self, request, view, obj):
        # print(request.data['profile'])
        print('UpdatePermission')
        # print(_is_in_group(obj,'Student'))
        if _is_in_group(request.user,'Super-admin'):
            return True
        if _is_in_group(request.user,'Teacher'):
            if (_is_in_group(obj,'Student')):
                return True
            return obj==request.user
        if _is_in_group(request.user,'Student'):
            return obj==request.user
        return False