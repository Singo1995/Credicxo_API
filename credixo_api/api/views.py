
from rest_framework import viewsets
from api.models import User
from api.serializers import UserSerializer
from api.permissions import CreatePermission,ListPermission,DeletePermission,RetrievePermission,UpdatePermission
from rest_framework.response import Response
from django.contrib.auth.models import Group

"""
_is_in_group is a function to check whether the user given is there is the specified group or not.
"""

def _is_in_group(user, group_name):
        """
        Takes a user and a group name, and returns `True` if the user is in that group.
        """
        try:
            return Group.objects.get(name=group_name).user_set.filter(id=user.id).exists()
        except Group.DoesNotExist:
            return None


"""
Using the model viewset for the view from the rest_framework
"""
class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer


    """
    Setting the permissions to acces the API's Created
    """
    def get_permissions(self):
        # print('self.action',self.action)
        permission_classes = []
        if self.action == 'create':
            permission_classes = [CreatePermission]
        elif self.action == 'update' or self.action == 'partial_update':
            permission_classes = [UpdatePermission]
        #list is a list view
        elif self.action == 'list':
            permission_classes = [ListPermission]
        elif self.action == 'destroy':
            permission_classes = [DeletePermission]
        #retrieve is a detailed view
        elif self.action == 'retrieve':
            permission_classes = [RetrievePermission]
        return [permission() for permission in permission_classes]

    """
    Overriding the list function to filter the  objects of students when the requested user is a Teacher.
    """    

    def list(self, request, *args, **kwargs):
        print('custom_list')
        if (_is_in_group(request.user, 'Teacher')):
            queryset = self.filter_queryset(User.objects.filter(groups__name='Student'))
        else:
            queryset = self.filter_queryset(self.get_queryset())
        # print('self.get_queryset()',self.get_queryset())
        # print(_is_in_group(request.user, 'Teacher'))
        # print(self.filter_queryset(self.get_queryset()))
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)