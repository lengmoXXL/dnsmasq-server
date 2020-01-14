from django.db import models

# Create your models here.


class DNSRecord(models.Model):

    ip = models.GenericIPAddressField()
    host = models.CharField(max_length=255)

    def __str__(self):
        return f'{self.ip}:{self.host}'