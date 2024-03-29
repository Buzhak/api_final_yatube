from rest_framework.routers import DefaultRouter

from django.urls import include, path

from .views import CommentViewSet, FollowViewSet, GroupViewSet, PostViewSet

router = DefaultRouter()
router.register(
    r'posts/(?P<post_id>[\w.@+-]+)/comments',
    CommentViewSet,
    basename='comments'
)
router.register('follow', FollowViewSet, basename='follow')
router.register('groups', GroupViewSet, basename='groups')
router.register('posts', PostViewSet)

urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
