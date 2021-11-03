from apps.blog.usecases import GetBlogsUseCase, GetRelationUseCase


class BlogsMixin:
    def get_blogs(self):
        return GetBlogsUseCase(
            blog_id=self.kwargs.get('blog_id')
        ).execute()


class RelationMixin:
    def get_relation(self):
        return GetRelationUseCase(
            relation_id=self.kwargs.get('relation_id')
        ).execute()
