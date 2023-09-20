from rest_framework import viewsets
from base.models import License, User, Machine, LicenseUsage
from .serializers import LicenseSerializer, UserSerializer, MachineSerializer, LicenseUsageSerializer

# Define ViewSets for the new models
class LicenseViewSet(viewsets.ModelViewSet):
    queryset = License.objects.all()
    serializer_class = LicenseSerializer

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

class MachineViewSet(viewsets.ModelViewSet):
    queryset = Machine.objects.all()
    serializer_class = MachineSerializer

class LicenseUsageViewSet(viewsets.ModelViewSet):
    queryset = LicenseUsage.objects.all()
    serializer_class = LicenseUsageSerializer
