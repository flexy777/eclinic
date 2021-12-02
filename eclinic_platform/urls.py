from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt import views as jwt_views
from eclinic_platform.views.appointment import AppointmentViewSet
from eclinic_platform.views.appointmentDetails import AppointmentDetailsViewSet

from eclinic_platform.views.categories import CategoriesViewSet
from eclinic_platform.views.communications import CommunicationViewSet
from eclinic_platform.views.favourite import FavouriteViewSet
from eclinic_platform.views.reviews import ReviewViewSet
from eclinic_platform.views.services import ServicesViewSet
from eclinic_platform.views.transactions import TransactionsViewSet
from eclinic_platform.views.users import  UserViewSet
from eclinic_platform.views.testimonial import TestimonialViewSet





router = DefaultRouter()
router.register(r'categories', CategoriesViewSet, 'categories'),
router.register(r'users', UserViewSet, 'users'),
router.register(r'testimonials', TestimonialViewSet, 'testimonials')
router.register(r'services',ServicesViewSet, 'services')
router.register(r'reviews', ReviewViewSet, 'reviews')
router.register(r'communications', CommunicationViewSet, 'communications')
router.register(r'favourites', FavouriteViewSet, 'favourites')
router.register(r'appointments', AppointmentViewSet, 'appointments')
router.register(r'appointment_details', AppointmentDetailsViewSet, 'appointment_details')
router.register(r'transactions', TransactionsViewSet, 'transactions')

urlpatterns = router.urls