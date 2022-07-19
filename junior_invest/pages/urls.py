from rest_framework.routers import DefaultRouter

from . import views

router = DefaultRouter()
router.register('pages', views.PageViewSet)
router.register('terms_files', views.TermsFileViewSet)

urlpatterns = router.urls