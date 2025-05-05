from rest_framework import routers

from core import views

router = routers.DefaultRouter()

router.register('user', views.UserViewSet, basename='user')
router.register('task', views.TaskViewSet, basename='task')

urlpatterns = router.urls
