from django.db import models

# Create your models here.
class Hotel(models.Model):
    name = models.CharField(max_length = 30, default = "", blank = False, null = True)
    star = models.DecimalField(default = 1, max_digits = 5, decimal_places=0, blank = False)
    latitude = models.IntegerField(blank = False, null = True)
    longitude = models.IntegerField(blank = False, null = True)
    photo = models.ImageField(upload_to = 'img', blank =True)
    opened_date = models.DateField(default =None, blank =True, null= True)
    entry = models.TimeField(auto_now = False, auto_now_add = False)
    departure = models.TimeField(auto_now = False, auto_now_add = False)
    owner = models.CharField(max_length = 30, default = "", blank = True, null= True)

    def __str__(self):
        return self.name
