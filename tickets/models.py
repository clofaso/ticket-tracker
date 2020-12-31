from django.db import models

# Create your models here.
class Ticket(models.Model):
    title = models.CharField(max_length=70)
    description = models.TextField(max_length=200)
    priority = models.PositiveSmallIntegerField(default='1')

    # def __str__(self):
    #     return self.title