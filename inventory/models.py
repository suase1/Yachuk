from django.db import models
from django.utils import timezone


class Post(models.Model):
    author1 = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title1 = models.CharField(max_length=200)
    text1 = models.TextField()
    created_date1 = models.DateTimeField(default=timezone.now)
    published_date1 = models.DateTimeField(blank=True, null=True)

    def publish(self):
        self.published_date1 = timezone.now()
        self.save()

    def __str__(self):
        return self.title
