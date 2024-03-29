from django.utils.datetime_safe import datetime
from rest_framework.exceptions import ValidationError

from apps.blog.models import Blogs, Relation
from apps.core.usecases import BaseUseCase

from django.utils.translation import gettext_lazy as _


class AddBlogUseCase(BaseUseCase):
    def __init__(self,
                 serializer):
        self.serializer = serializer
        self.data = serializer.validated_data

    def execute(self):
        self._factory()

    def _factory(self):
        self._blog = Blogs(**self.data)
        self._blog.save()


class ListBlogsUseCase(BaseUseCase):

    def execute(self):
        self._factory()
        return self._blogs

    def _factory(self):
        self._blogs = Blogs.objects.all()


class GetBlogsUseCase(BaseUseCase):
    def __init__(self, blog_id):
        self._blog_id = blog_id

    def execute(self):
        self._factory()
        return self._blog

    def _factory(self):
        try:
            self._blog = Blogs.objects.get(pk=self._blog_id)
        except Blogs.DoesNotExist:
            raise ValidationError({'error': _('Blogs  does not exist for following id.')})


class UpdateBlogsUseCase(BaseUseCase):
    def __init__(self, serializer, blogs: Blogs):
        self.serializer = serializer
        self._data = serializer.validated_data
        self._blogs = blogs

    def execute(self):
        self._factory()

    def _factory(self):
        for key in self._data.keys():
            setattr(self._blogs, key, self._data.get(key))
        self._blogs.updated_at = datetime.now()
        self._blogs.save()


class DeleteBlogUseCase(BaseUseCase):
    def __init__(self, blogs):
        self._blogs = blogs

    def execute(self):
        self._factory()

    def _factory(self):
        self._blogs.delete()


class AddRelationUseCase(BaseUseCase):
    def __init__(self,
                 serializer):
        self.serializer = serializer
        self.data = serializer.validated_data

    def execute(self):
        self._factory()

    def _factory(self):
        self._relation = Relation(**self.data)
        print(self._relation)
        self._relation.save()


class ListRelationUseCase(BaseUseCase):

    def execute(self):
        self._factory()
        return self._relation

    def _factory(self):
        self._relation = Relation.objects.all()


class GetRelationUseCase(BaseUseCase):
    def __init__(self, relation_id):
        self._relation_id = relation_id

    def execute(self):
        self._factory()
        return self.relation

    def _factory(self):
        try:
            self.relation = Relation.objects.get(pk=self._relation_id)
        except Relation.DoesNotExist:
            raise ValidationError({'error': _('Relation  does not exist for following id.')})


class UpdateRelationUseCase(BaseUseCase):
    def __init__(self, serializer, relation: Relation):
        self.serializer = serializer
        self._data = serializer.validated_data
        self._relation = relation

    def execute(self):
        self._factory()

    def _factory(self):
        for key in self._data.keys():
            setattr(self._relation, key, self._data.get(key))
        self._relation.updated_at = datetime.now()
        self._relation.save()


class DeleteRelationUseCase(BaseUseCase):
    def __init__(self, relation):
        self._relation = relation

    def execute(self):
        self._factory()

    def _factory(self):
        self._relation.delete()
