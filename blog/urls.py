from rest_framework import routers
from .api import PostViewSet

router = routers.DefaultRouter()

router.register('api/posts', PostViewSet, 'Posts')

urlpatterns = router.urls