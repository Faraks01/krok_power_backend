from rest_framework import routers
from .views import *

app_name = 'news'

router = routers.SimpleRouter()

router.register(r'news', NewsViewSet, basename='news')

urlpatterns = router.urls
