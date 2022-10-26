from tokenize import group
from rest_framework import viewsets , mixins, exceptions, permissions
from django.shortcuts import get_object_or_404
from rest_framework import filters

from .serializers import CommentSerializer, FollowSerializer, GroupSerializer, PostSerializer
from posts.models import Comment, Follow, Group, Post, User 


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def perform_create(self, serializer):
            serializer.save(
                author=self.request.user,
            )
  

    def perform_update(self, serializer):
        if serializer.instance.author != self.request.user:
            raise exceptions.PermissionDenied(
                'Изменение чужого контента запрещено!'
            )
        super(PostViewSet, self).perform_update(serializer)

    def perform_destroy(self, serializer):
        if serializer.author != self.request.user:
            raise exceptions.PermissionDenied(
                'Изменение чужого контента запрещено!'
            )
        super(PostViewSet, self).perform_destroy(serializer)


class FollowViewSet(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    serializer_class = FollowSerializer
    filter_backends = (filters.SearchFilter,)
    search_fields = ('following__username',) 

    def get_user(self):
        return get_object_or_404(User, username=self.request.user)

    def get_queryset(self):
        user = self.get_user()
        return Follow.objects.filter(user=user)

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)


class GroupViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)
