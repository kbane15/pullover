from django.shortcuts import render_to_response
from pullover.locater.models import Intro
from pullover.locater.models import Town
from pullover.information.models import Entertainment
from pullover.information.models import Food

def home(request):
    greeting = "Pull Into New, Exciting Towns"
    graph = Intro.objects.all()[:5]
    towns = Town.objects.all()[:7]
    return render_to_response('home.html', {
        'towns': towns,
        'greeting': greeting,
        'graph': graph,
    })

def detail(request, town_id):
    town = Town.objects.get(id=town_id)
    ent = Entertainment.objects.filter(town=town)
    food = Food.objects.filter(town=town)
    return render_to_response('detail.html', {
        'town': town,
        'ent': ent,
        'food': food,
    })
