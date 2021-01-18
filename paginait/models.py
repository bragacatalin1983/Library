from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class Cursit(models.Model):
    title = models.CharField(max_length=100)
    date = models.DateTimeField(default=datetime.now(), blank=True)
    url = models.URLField(blank=None)
    img = models.ImageField(upload_to='media/picturesIT')
    description = models.TextField()
    isliked = models.ManyToManyField(
        User, default=None, blank=True, related_name='itlikes')

    def __str__(self):
        return self.title

    @property
    def num_likes(self):
        return self.isliked.all().count()


LIKE_CHOICES = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike'),
)


class Liked(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='ituser')
    blog = models.ForeignKey(
        Cursit, on_delete=models.CASCADE, related_name='itpost')
    value = models.CharField(choices=LIKE_CHOICES,
                             default='Like', max_length=10)

    def __str__(self):
        return self.blog
