from django.db import models
from django.contrib.auth.models import User
from django.contrib.postgres.fields import ArrayField


class Item(models.Model):
    id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=4000, null=True)
    stock = models.IntegerField(default=0)
    price = models.FloatField(null=True)
    size = ArrayField(
            models.CharField(blank=True, max_length=50),
            size=8, null=True
        )
    image = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True, editable=False, null=True)

    def __str__(self):
        return self.name