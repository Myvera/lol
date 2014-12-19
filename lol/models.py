from django.db import models

# Create your models here.

class LOL(models.Model):
    name_text = models.CharField(max_length=50)
    level = models.IntegerField()
    summoner_id = models.CharField(max_length=50)




