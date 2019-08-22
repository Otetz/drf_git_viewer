from django.db import models


# Create your models here.

class LastCommit(models.Model):
    commit = models.CharField('commit', max_length=255, unique=True)
    commit_date = models.DateTimeField('commit_date')
    branch = models.CharField('branch', max_length=1024)
    version = models.CharField('version', max_length=255)
    started = models.DateTimeField('started')
    uptime_seconds = models.IntegerField('uptime_seconds')
