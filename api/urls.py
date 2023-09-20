from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(r'licenses', views.LicenseViewSet)
router.register(r'users', views.UserViewSet)
router.register(r'machines', views.MachineViewSet)
router.register(r'license-usage', views.LicenseUsageViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
