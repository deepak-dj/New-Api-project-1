from django.db import models


class Students(models.Model):
    FirstName = models.CharField(max_length=30)
    LastName = models.CharField(max_length=30)
    Subject = models.CharField(max_length=40)
    Marks = models.IntegerField()
    # Image = models.ImageField(upload_to='/image/')

    def __str__(self):
        return self.FirstName
