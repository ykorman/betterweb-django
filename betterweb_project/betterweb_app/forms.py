from django import forms
from betterweb_app.models import Deposit

class DepositForm(forms.ModelForm):
    giver = forms.IntegerField(widget=forms.HiddenInput())
    when = forms.DateTimeField(widget=forms.HiddenInput())
    amount = forms.IntegerField(initial=50)
    
    class Meta:
        model = Deposit
        fields = ('giver', 'when', 'amount')
