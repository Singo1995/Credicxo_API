from rest_framework import serializers
from api.models import User,UserProfile
from django.contrib.auth.models import Group

"""
Serializer for the UserProfile
"""
class UserProfileSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = UserProfile
        fields = ['group']
"""
serializer for the user
"""

class UserSerializer(serializers.HyperlinkedModelSerializer):
    profile = UserProfileSerializer(required=True)

    class Meta:
        model = User
        fields = ['url', 'email', 'first_name', 'last_name', 'password', 'profile']
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        # print('Validated Data',validated_data['profile'].get('group'))
        """
        Getting the group from the user like super-admin,teacher and student.
        """
        group = validated_data['profile'].get('group')
        profile_data = validated_data.pop('profile')
        password = validated_data.pop('password')
        user = User(**validated_data)
        user.set_password(password)
        user.save()
        """
        After the creation of the user he is added to a particular group.
        """
        user.groups.add(Group.objects.get(name=group))
        UserProfile.objects.create(user=user, **profile_data)
        return user

    def update(self, instance, validated_data):
        profile_data = validated_data.pop('profile')
        profile = instance.profile

        instance.email = validated_data.get('email', instance.email)
        instance.save()

        profile.text = profile_data.get('group', profile.group)
        profile.save()

        return instance