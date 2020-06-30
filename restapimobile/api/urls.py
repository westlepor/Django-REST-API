from rest_framework import routers
from django.urls import path
from . import views
from django.conf.urls import include

router = routers.DefaultRouter()
router.register(r'customer', views.CustomerViewSet)
router.register(r'device', views.DeviceViewSet)
router.register(r'task', views.TaskViewSet)

urlpatterns = [
    path('', include(router.urls)),
]