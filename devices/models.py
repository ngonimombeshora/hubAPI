from django.db import models

# Create your models here. example model to work with


class Device(models.Model):
    name = models.CharField(max_length=100, blank=False, default='device name')
    category = models.CharField(max_length=100, blank=False, default='sensor')
    location = models.CharField(max_length=100, blank=True, default='')
    device_id = models.CharField(max_length=100, blank=True, default='1')
    status = models.CharField(max_length=100, blank=True, default='')
    created = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey(
        'auth.User', related_name='devices', on_delete=models.CASCADE, default="not set")

    def __str__(self):
        """Return a human readable representation of the model instance."""
        return "{}".format(self.name)

    class Meta:
        ordering = ('created',)
