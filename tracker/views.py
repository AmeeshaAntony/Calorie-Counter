from django.shortcuts import render, redirect
from .models import FoodItem
from .forms import FoodItemForm

def food_list(request):
    foods = FoodItem.objects.all()
    return render(request, 'tracker/food_list.html', {'foods': foods})

def add_food(request):
    if request.method == 'POST':
        form = FoodItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('food_list')
    else:
        form = FoodItemForm()
    return render(request, 'tracker/add_food.html', {'form': form})

def view_calories(request):
    food_items = FoodItem.objects.all()
    total_calories = sum(item.calories for item in food_items)
    #context = {'food_items': food_items, 'total_calories': total_calories}
    return render(request, 'tracker/view_calories.html')

