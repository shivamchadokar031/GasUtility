from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

class ServiceRequestType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class ServiceRequest(models.Model):
    customer = models.ForeignKey(User, on_delete=models.CASCADE) 
    request_type = models.ForeignKey(ServiceRequestType, on_delete=models.CASCADE)
    details = models.TextField()
    status = models.CharField(max_length=50, default='Pending') 
    files = models.FileField(upload_to='service_requests/', null=True, blank=True)
    submitted_at = models.DateTimeField(default=timezone.now)
    resolved_at = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"Request by {self.customer.username} for {self.request_type.name}"

class Customer(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    address = models.CharField(max_length=255)

    def __str__(self):
        return self.user.username

class SupportRepresentative(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    assigned_requests = models.ManyToManyField(ServiceRequest, blank=True)

    def __str__(self):
        return self.user.username
