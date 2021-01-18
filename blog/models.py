from django.db import models
from datetime import datetime
from django.contrib.auth.models import User


class Blog(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    url = models.URLField(blank=None)
    img = models.ImageField(upload_to='media/pictures')
    date = models.DateTimeField(default=datetime.now(), blank=True)
    liked = models.ManyToManyField(
        User, default=None, blank=True, related_name='bloglikes')

    def __str__(self):
        return self.title

    @property
    def num_likes(self):
        return self.liked.all().count()


LIKE_CHOICES = (
    ('Like', 'Like'),
    ('Unlike', 'Unlike'),
)


class Like(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    value = models.CharField(choices=LIKE_CHOICES,
                             default='Like', max_length=10)

    def __str__(self):
        return self.blog
