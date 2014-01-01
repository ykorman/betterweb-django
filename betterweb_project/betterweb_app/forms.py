from django import forms
from betterweb_app import models

class DepositForm(forms.ModelForm):
    class Meta:
        model = Deposit
        fields = ('amount')