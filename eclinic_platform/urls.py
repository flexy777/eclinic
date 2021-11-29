from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt import views as jwt_views

from eclinic_platform.views.categories import CategoriesViewSet
from eclinic_platform.views.users import  UserViewSet
from eclinic_platform.views.testimonial import TestimonialViewSet



router = DefaultRouter()
router.register(r'categories', CategoriesViewSet, 'categories'),
router.register(r'users', UserViewSet, 'users'),
router.register(r'testimonials', TestimonialViewSet, 'testimonials')


urlpatterns = router.urls