from rest_framework.routers import DefaultRouter

from django.urls import include, path

from .views import CommentViewSet, FollowViewSet, GroupViewSet,PostViewSet

routes = DefaultRouter()
routes.register('comments', CommentViewSet)
routes.register('follow', FollowViewSet, basename='follow')
routes.register('groups', GroupViewSet, basename='groups')
routes.register('posts', PostViewSet)

urlpatterns = [
    path('v1/', include(routes.urls)),
    path('v1/', include('djoser.urls')),
    path('v1/', include('djoser.urls.jwt')),
]
