
from rest_framework import routers
from api.views import UserViewSet
from django.urls import path,include
"""
Using the default router
GET /api/users/ to list
GET /api/users/1
DELETE /api/users/1
etc
"""
router = routers.DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('auth/', include('rest_auth.urls')),
    path('password_reset/', include('django_rest_passwordreset.urls', namespace='password_reset')),
]