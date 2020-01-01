from django.conf import settings
from django.db import models


# Create your models here.
def upload_status_image(instance, filename):
    return 'updates/{user}/{filename}'.format(user=instance.user, filename=filename)


class StatusQuerySet(models.QuerySet):
    pass


class StatusManager(models.Manager):
    def get_queryset(self):
        return StatusQuerySet(self.model, using=self._db)


class Status(models.Model):  # just like fb status, instagram post, tweet, linkedln status
    user = models.ForeignKey(settings.AUTH_USER_MODEL)
    content = models.TextField(null=True, blank=True)
    image = models.ImageField(upload_to=upload_status_image)
    updated = models.DateTimeField(auto_now=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.content)[:50]
