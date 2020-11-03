from django import forms


class GuessForm(forms.Form):
    guess = forms.CharField(label='Enter your guess', max_length=100)