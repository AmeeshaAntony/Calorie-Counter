from django.shortcuts import render, redirect
from .models import FoodItem

def add_food(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        calories = request.POST.get('calories')
        FoodItem.objects.create(name=name, calories=calories)
        return redirect('calorie_counter:home')
    return render(request, 'tracker/add_food.html')

def view_calories(request):
    food_items = FoodItem.objects.all()
    total_calories = sum(item.calories for item in food_items)
    #context = {'food_items': food_items, 'total_calories': total_calories}
    return render(request, 'tracker/view_calories.html')

