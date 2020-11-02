from django.shortcuts import render, redirect
from django.urls import reverse

from game.models import Tune


def index(request):
    current_tune = Tune.objects.order_by('-date').first()
    return redirect(reverse(specific, args=[current_tune]))


def specific(request, date):
    curr_tune = Tune.objects.get(date=date)
    context = {
        'curr_tune': curr_tune,
        'all_tunes': Tune.objects.order_by('-date') ,
        'active': curr_tune == Tune.objects.order_by('-date').first()
    }
    return render(request, 'game/guesser.html', context)
