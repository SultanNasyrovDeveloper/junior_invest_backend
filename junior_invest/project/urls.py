from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register('projects', views.ProjectViewSet)
router.register('categories', views.ProjectCategoryViewSet)
router.register('votes', views.ProjectVoteViewSet)
router.register('images', views.ProjectImageViewSet)
router.register('media', views.ProjectMediaViewSet)

urlpatterns = router.urls
