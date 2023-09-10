from django.db import models


class Worker(models.Model):
    picture = models.ImageField(upload_to='worker_pictures')
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)

    def __str__(self):
        return self.name

