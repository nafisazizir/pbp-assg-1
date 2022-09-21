from django.db import models

class MyWatchListItem(models.Model):
    watched = models.CharField(max_length=255)
    title = models.TextField()
    rating = models.FloatField()
    release_date = models.TextField()
    review = models.TextField()