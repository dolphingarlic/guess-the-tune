from django import forms
from fuzzywuzzy import fuzz


class GuessForm(forms.Form):
    guess = forms.CharField(label='Enter your guess', max_length=100)

    def __init__(self, *args, **kwargs):
        self.tune = kwargs.pop('tune')
        super(GuessForm, self).__init__(*args, **kwargs)

    def clean(self):
        token_set_ratio = fuzz.token_set_ratio(self.tune.answer, self.cleaned_data['guess'])
        if token_set_ratio < 85:
            raise forms.ValidationError('Incorrect guess. Please try again.')
        return self.cleaned_data
