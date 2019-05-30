from django.db import models


class BaseModel(models.Model):
    created_time = models.DateTimeField(auto_now_add=True, blank=True)
    updated_time = models.DateTimeField(auto_now=True, null=True, blank=True)

    class Meta:
        abstract = True
