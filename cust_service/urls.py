from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register_view, name='register'),
    path('', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('submit/', views.submit_service_request, name='submit_service_request'),
    path('track/', views.track_service_requests, name='track_service_requests'),
    path('requests/<int:pk>/', views.service_request_detail, name='service_request_detail'),
    path('support/manage/', views.manage_requests, name='manage_requests'),
]
