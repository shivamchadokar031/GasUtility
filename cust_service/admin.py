from django.contrib import admin
from .models import ServiceRequest, ServiceRequestType, Customer, SupportRepresentative

admin.site.register(ServiceRequest)
admin.site.register(ServiceRequestType)
admin.site.register(Customer)
admin.site.register(SupportRepresentative)
