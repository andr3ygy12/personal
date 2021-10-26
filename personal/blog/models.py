from django.db import models
from django.contrib.auth.models import User


# Create your models here.
STATUS = (
    (0, 'Draft'),
    (1, 'Publish')
)
class Post (models.Model):
    title = models.CharField(max_length=100, unique=True)
    image = models.ImageField(blank=True, upload_to='images/')
    slug = models.SlugField(max_length=200, unique=True)
    author = models.ForeignKey(
        User,
        models.CASCADE,
        related_name = "blog_posts"
    )
    updated_on = models.DateTimeField(auto_now = True)
    content = models.TextField()
    created_on = models.DateTimeField(auto_now_add = True)
    status = models.IntegerField(
        choices=STATUS,
        default = 0
    )

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.title


# This is a class to allows the app use and save comments
class Comment (models.Model):
    Post = models.ForeignKey(
        Post, on_delete = models.CASCADE, related_name = "comments"
    )
    name = models.CharField(max_length=100)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=False)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return 'Comentario: {} by {}'.format(self.body, self.name)