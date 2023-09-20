from django.db import models

class License(models.Model):
    name = models.CharField(max_length=200)
    total_licenses = models.PositiveIntegerField()
    licenses_in_use = models.PositiveIntegerField()
    expiry_date = models.DateField()

class User(models.Model):
    name = models.CharField(max_length=200)

class Machine(models.Model):
    name = models.CharField(max_length=200)

class LicenseUsage(models.Model):
    license = models.ForeignKey(License, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    machine = models.ForeignKey(Machine, on_delete=models.CASCADE)
