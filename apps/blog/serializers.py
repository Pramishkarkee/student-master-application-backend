from rest_framework import serializers

from apps.blog.models import Blogs, Relation


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blogs
        fields = '__all__'


class RelationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Relation
        fields = '__all__'


class AddBlogSerializer(BlogSerializer):
    class Meta(BlogSerializer.Meta):
        fields = (
            'title',
            'relation',
            'image',
            'content',
            'author_name',
        )


class ListBlogSerializer(BlogSerializer):
    class Meta(BlogSerializer.Meta):
        fields = (
            'id',
            'title',
            'relation',
            'image',
            'content',
            'author_name',
            'created_at',
            'updated_at',
        )


class UpdateBlogSerializer(AddBlogSerializer):
    pass


class AddRelationSerializer(RelationSerializer):
    class Meta(RelationSerializer.Meta):
        fields = (
            'name',
        )


class ListRelationSerializer(RelationSerializer):
    class Meta(RelationSerializer.Meta):
        fields = (
            'id',
            'name',
            'created_at',
            'updated_at',
        )



class UpdateRelationSerialzier(AddRelationSerializer):
    pass