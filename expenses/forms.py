from django import forms
from .models import Expense
# from django.contrib.auth.forms import UserCreationForm
# from django.contrib.auth.models import User


class ExpenseSearchForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ('name', 'category', 'amount', 'date')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['name'].required = False
        self.fields['category'].required = False
        self.fields['amount'].required = False
        self.fields['date'].required = False


"""
class DateSearchForm(forms.ModelForm):
    start_date = forms.DateTimeField(required=False)
    end_date = forms.DateTimeField(required=False)

    class Meta:
        model = Expense
        fields = ('name', 'category', 'amount', 'start_date', 'end_date')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['start_date'].required = False
        self.fields['end_date'].required = False
"""