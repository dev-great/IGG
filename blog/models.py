from django.db import models
from cloudinary.models import CloudinaryField
# Create your models here.


class Banner(models.Model):
    title = models.CharField(max_length=1000)
    BannerImage = CloudinaryField('image', resource_type="image",)

    def __str__(self):
        return self.title


class FeedPost(models.Model):
    title = models.CharField(max_length=1000)
    uri = models.CharField(max_length=1000)
    PostImage = CloudinaryField('image', resource_type="image",)
    author = models.CharField(max_length=500)
    publisheddate = models.DateTimeField(auto_now_add=True)
    updateddate = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('-publisheddate',)

    def __str__(self):
        return self.title[:100]
