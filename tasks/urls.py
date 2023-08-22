from rest_framework.routers import DefaultRouter
from .views import TasksAPI

router = DefaultRouter()
router.register("tasks", TasksAPI, basename="tasks")
urlpatterns = router.urls
