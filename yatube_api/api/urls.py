from django.urls import path, include
from rest_framework.routers import SimpleRouter

from api.views import CommentViewSet, GroupViewSet, PostViewSet


router = SimpleRouter()

router.register(r'posts', PostViewSet, basename='posts')
router.register('posts/(?P<post_id>\\d+)/comments', CommentViewSet,
                basename='comments')
router.register(r'groups', GroupViewSet, basename='groups')


urlpatterns = [
    path('v1/', include(router.urls))
]
