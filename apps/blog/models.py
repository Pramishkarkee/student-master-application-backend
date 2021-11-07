from django.db import models

# Create your models here.
from apps.blog.utils import upload_blog_image_to
from apps.core.models import BaseModel
from apps.core.validators import validate_image


class Relation(BaseModel):
    name = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Blogs(BaseModel):
    relation = models.ForeignKey(to=Relation, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    author_name = models.CharField(max_length=100)
    content = models.TextField()
    image = models.ImageField(upload_to=upload_blog_image_to,
                              default='consultancy/logo/default_logo.png',
                              validators=[validate_image]
                              )

    def __str__(self):
        return self.title
