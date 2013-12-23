from django.contrib import admin
from betterweb_app.models import *

for model in ( Giver, Receiver, Deposit, Withdrawal, Tip, Art, TipToArt ):
    admin.site.register(model)