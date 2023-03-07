from django.db import models

# Create your models here.
class Movie(models.Model):
    #id son autogenerados
    title = models.CharField(max_length=100)
    description = models.TextField()
    years = models.IntegerField()
    rating = models.FloatField()
    genre = models.CharField(max_length=50)
    country = models.CharField(max_length=50)
    duration = models.IntegerField()
    prince = models.FloatField()
    created_at = models.DateTimeField(auto_now=True)
    update_at = models.DateField(null=True)
    
    class Meta:
        db_table = 'movies'