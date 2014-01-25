from datetime import datetime

from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required

from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from betterweb_app.serializers import UserSerializer, GroupSerializer, TipSerializer

from betterweb_app.models import Tip

# django rest framework quickstart code 
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
# end of quickstart code

class TipViewSet(viewsets.ModelViewSet):
  queryset = Tip.objects.all()
  serializer_class = TipSerializer

from betterweb_app.forms import DepositForm

def index(request):
    if request.user.is_authenticated() and request.user.username == 'admin':
        logout(request)
    #if not request.user.is_authenticated():
    #    #return redirect('/login/?next=%s' % request.path)
    #    return HttpResponse("Hello, world. You're at the bw index.")
    return render(request, 'betterweb_app/index.html')

def register(request):
    return HttpResponse("Hello, world. You're at the bw register.")

@login_required
def home(request):
    return render(request, 'betterweb_app/home.html')

@login_required
def deposit(request):
    context = RequestContext(request)
    if request.method == 'POST':
        form = DepositForm(request.POST)
        if form.is_valid():
            deposit = form.save(commit=False)
            deposit.giver = request.user.giver
            deposit.save()
            request.user.giver.balance += deposit.amount
            request.user.giver.save()
            return home(request)
        else:
            print request.POST
            print form.errors
    else:
        form = DepositForm()
    return render_to_response('betterweb_app/deposit.html', {'form': form}, context)

@login_required
def withdraw(request):
    return HttpResponse("Hello, %s. You're at the bw withdraw." % username)