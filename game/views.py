from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse

from game.models import Tune
from game.forms import GuessForm


def index(request):
    current_tune = Tune.objects.order_by('-date').first()
    return redirect(reverse(specific, args=[current_tune]))


def specific(request, date):
    curr_tune = get_object_or_404(Tune, date=date)
    form = GuessForm(tune=curr_tune)

    if request.method == 'POST':
        form = GuessForm(request.POST, tune=curr_tune)
        if form.is_valid():
            assert request.user.is_authenticated
            curr_tune.successful_guessers.add(request.user)

    context = {
        'curr_tune': curr_tune,
        'all_tunes': Tune.objects.order_by('-date'),
        'form': form,
    }
    return render(request, 'game/guesser.html', context)


def editor(request):
    return render(request, 'game/editor.html');