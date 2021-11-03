from django.shortcuts import render
from django.utils.translation import gettext_lazy as _

# Create your views here.
from apps.blog import serializers, usecases
from apps.blog.mixins import BlogsMixin, RelationMixin
from apps.core import generics


class AddBlogsView(generics.CreateWithMessageAPIView):
    """
    Use this end-point to add blogs
    """
    serializer_class = serializers.AddBlogSerializer
    message = 'Created successfully'

    def perform_create(self, serializer):
        return usecases.AddBlogUseCase(serializer=serializer).execute()


class ListBlogsView(generics.ListAPIView):
    """
    Use this end-point to List  all  blogs
    """
    serializer_class = serializers.ListBlogSerializer
    no_content_error_message = _('No blogs at the moment')

    def get_queryset(self):
        return usecases.ListBlogsUseCase().execute()


class DeleteBlogView(BlogsMixin, generics.DestroyAPIView):
    """
    Use this endpoint to delete blogs
    """

    def get_object(self):
        return self.get_blogs()

    def perform_destroy(self, instance):
        return usecases.DeleteBlogUseCase(
            blogs=self.get_object(),
        ).execute()


class UpdateBlogView(generics.UpdateAPIView, BlogsMixin):
    """
    Use this end-point to Update   blogs.
    """

    serializer_class = serializers.UpdateBlogSerializer
    queryset = ''

    # permission_classes = (IsAdminUser,)

    def get_object(self):
        return self.get_blogs()

    def perform_update(self, serializer):
        return usecases.UpdateBlogsUseCase(
            serializer=serializer,
            blogs=self.get_object()
        ).execute()


class AddRelationView(generics.CreateWithMessageAPIView):
    """
    Use this end-point to add relation
    """
    serializer_class = serializers.AddRelationSerializer
    message = 'Created successfully'

    def perform_create(self, serializer):
        return usecases.AddRelationUseCase(serializer=serializer).execute()


class ListRelationView(generics.ListAPIView):
    """
    Use this end-point to List  all  relation
    """
    serializer_class = serializers.ListRelationSerializer
    no_content_error_message = _('No relation at the moment')

    def get_queryset(self):
        return usecases.ListRelationUseCase().execute()


class DeleteRelationView(RelationMixin, generics.DestroyAPIView):
    """
    Use this endpoint to delete relation
    """

    def get_object(self):
        return self.get_relation()

    def perform_destroy(self, instance):
        return usecases.DeleteRelationUseCase(
            relation=self.get_object(),
        ).execute()


class UpdateRelationView(generics.UpdateAPIView, RelationMixin):
    """
    Use this end-point to Update   relations.
    """

    serializer_class = serializers.UpdateRelationSerialzier
    queryset = ''

    # permission_classes = (IsAdminUser,)

    def get_object(self):
        return self.get_relation()

    def perform_update(self, serializer):
        return usecases.UpdateRelationUseCase(
            serializer=serializer,
            relation=self.get_object()
        ).execute()
