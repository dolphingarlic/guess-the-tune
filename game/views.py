from django.shortcuts import render, redirect
from django.urls import reverse
from fuzzywuzzy import fuzz

from game.models import Tune


def index(request):
    current_tune = Tune.objects.order_by('-date').first()
    return redirect(reverse(specific, args=[current_tune]))


def specific(request, date):
    curr_tune = Tune.objects.get(date=date)
    incorrect = False

    if request.method == 'POST':
        print(request.POST)
        guess = request.POST.get('guess')
        token_sort_ratio = fuzz.token_sort_ratio(curr_tune.answer, guess)
        print(guess, token_sort_ratio)
        if token_sort_ratio > 95:
            assert request.user.is_authenticated
            curr_tune.successful_guessers.add(request.user)
        else:
            incorrect = True

    context = {
        'curr_tune': curr_tune,
        'all_tunes': Tune.objects.order_by('-date'),
        'active': curr_tune == Tune.objects.order_by('-date').first(),
        'incorrect': incorrect,
    }
    return render(request, 'game/guesser.html', context)
