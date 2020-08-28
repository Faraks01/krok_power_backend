from rest_framework import routers
from .views import *

app_name = 'from'

router = routers.SimpleRouter()

router.register(r'feedback_forms', FeedbackFormViewSet, basename='feedback_form')
router.register(r'billing_forms', BillingFormViewSet, basename='billing_form')
router.register(r'colors', ColorViewSet, basename='color')
router.register(r'body_shapes', BodyShapeViewSet, basename='body_shape')
router.register(r'manufacturers', ManufacturerViewSet, basename='manufacturer')
router.register(r'wire_types', WireTypeViewSet, basename='wire_type')

urlpatterns = router.urls
