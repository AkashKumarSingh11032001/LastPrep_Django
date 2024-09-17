from django.db import models

# Create your models here.
class HostInfo(models.Model):
    host_type = [
        {'a','host 1'},
        {'b','host 2'},
        {'c','host 3'},
        {'d','host 4'},
    ]
    hostname = models.CharField(max_length=64,unique=True)
    ipaddr = models.GenericIPAddressField(unique=True)
    port = models.IntegerField(default=22)
    status = models.BooleanField(default=True)
    memo = models.TextField(blank=True,null=True)
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)
    type = models.CharField(max_length=2, choices=host_type)

    def __str__(self):
        return self.hostname