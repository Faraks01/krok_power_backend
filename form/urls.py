from rest_framework import routers
from .views import *

app_name = 'product'

router = routers.SimpleRouter()

router.register(r'feedback_forms', FeedbackFormViewSet, basename='feedback_form')
router.register(r'billing_forms', BillingFormViewSet, basename='billing_form')

urlpatterns = router.urls
