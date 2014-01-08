from django import forms
from betterweb_app.models import Deposit

class DepositForm(forms.ModelForm):
    amount = forms.NumberInput(attrs={'class': 'form-control',})
    class Meta:
        model = Deposit
        fields = ('amount',)
