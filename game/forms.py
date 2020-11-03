from django import forms
from fuzzywuzzy import fuzz


class GuessForm(forms.Form):
    guess = forms.CharField(label='Enter your guess', max_length=100)

    def __init__(self, *args, **kwargs):
        self.tune = kwargs.pop('tune')
        super(GuessForm, self).__init__(*args, **kwargs)

    def clean(self):
        token_sort_ratio = fuzz.token_sort_ratio(self.tune.answer, self.cleaned_data['guess'])
        if token_sort_ratio < 90:
            print('Raised error!')
            raise forms.ValidationError('Incorrect guess. Please try again.')
        return self.cleaned_data