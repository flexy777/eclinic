from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt import views as jwt_views

from eclinic_platform.views.categories import CategoriesViewSet



router = DefaultRouter()
router.register(r'categories', CategoriesViewSet, 'categories')


urlpatterns = router.urls