from rest_framework import routers
from django.urls import path
from . import views
from django.conf.urls import include

router = routers.DefaultRouter()
router.register(r'customer', views.CustomerViewSet)
router.register(r'device', views.DeviceViewSet)
router.register(r'task', views.TaskViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
    path('api/available_task/<device_id>', views.AvailableTaskView.as_view()),
    path('api/execute/<device_id>/<task_id>', views.ExecutedTaskView.as_view()),
    path('api/result/<device_id>/<task_id>/<result>', views.ResultTaskView.as_view())
]