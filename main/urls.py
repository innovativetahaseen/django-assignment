from django.urls import path
from . import views

urlpatterns = [
    path('', views.login_view),
    path('dashboard/', views.dashboard),
    path('form/', views.exam_form),
    path('success/', views.success),
]