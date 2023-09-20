from rest_framework import serializers
from base.models import License, User, Machine, LicenseUsage



class LicenseSerializer(serializers.ModelSerializer):
    class Meta:
        model = License
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class MachineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Machine
        fields = '__all__'

class LicenseUsageSerializer(serializers.ModelSerializer):
    class Meta:
        model = LicenseUsage
        fields = '__all__'
