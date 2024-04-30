# models.py
from django.db import models
import pymongo

# url = "mongodb+srv://samitsinghvi:samit16MONGO@cluster0.v5kwwe5.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
# client = pymongo.MongoClient(url)
# db = client['HealthTracker']


class UserNutrientData(models.Model):
    username = models.CharField(max_length=100)
    carbohydrates_total_g = models.FloatField(default=0)
    cholesterol_mg = models.FloatField(default=0)
    fat_saturated_g = models.FloatField(default=0)
    fat_total_g = models.FloatField(default=0)
    fiber_g = models.FloatField(default=0)
    potassium_mg = models.FloatField(default=0)
    protein_g = models.FloatField(default=0)
    sodium_mg = models.FloatField(default=0)
    sugar_g = models.FloatField(default=0)
