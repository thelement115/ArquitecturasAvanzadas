from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'singup', views.SingUp, basename='Registro')
router.register(r'singin', views.LoginViewSet, basename='Login')

urlpatterns = router.urls