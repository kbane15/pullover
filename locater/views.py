from django.shortcuts import render_to_response
from pullover.locater.models import Intro
from pullover.locater.models import Town
from pullover.information.models import Entertainment
from pullover.information.models import Food
from pullover.information.models import History

def home(request):
    greeting = "Pull Into New, Exciting Towns"
    graph = Intro.objects.all()[:5]
    towns = Town.objects.all()[:14]
    return render_to_response('home.html', {
        'towns': towns,
        'greeting': greeting,
        'graph': graph,
    })

def detail(request, town_id):
    town = Town.objects.get(id=town_id)
    entsub = "Entertainment"
    ent = Entertainment.objects.filter(town=town)
    foodsub = "Food"
    food = Food.objects.filter(town=town)
    historysub = "History"
    history = History.objects.filter(town=town)
    return render_to_response('detail.html', {
        'town': town,
        'ent': ent,
        'food': food,
        'history': history,
        'entsub': entsub,
        'foodsub': foodsub,
        'historysub': historysub,
    })
