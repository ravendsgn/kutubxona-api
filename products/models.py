from django.db import models

# Create your models here.


class Books(models.Model):
    name = models.CharField(max_length=200)
    desc = models.CharField(max_length=200)
    author = models.CharField(max_length=200)
    year_of_publication = models.IntegerField()
    isbn = models.CharField(max_length=12)

    def __str__(self):
        return self.name
