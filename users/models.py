from django.db import models


# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=100, null=False)
    age = models.IntegerField(null=False)
    email = models.CharField(max_length=200, blank=True, default='')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created']
