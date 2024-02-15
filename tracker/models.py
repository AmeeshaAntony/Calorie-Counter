from django.db import models

class FoodItem(models.Model):
    name = models.CharField(max_length=100)
    calories = models.IntegerField()
    date_consumed = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.name
