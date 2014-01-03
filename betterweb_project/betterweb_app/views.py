from datetime import datetime

from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from django.contrib.auth.decorators import login_required

from betterweb_app.forms import DepositForm

def index(request):
    return HttpResponse("Hello, world. You're at the bw index.")

def register(request):
    return HttpResponse("Hello, world. You're at the bw register.")

def landing(request):
    print request.user.is_authenticated()
    if not request.user.is_authenticated():
        return redirect('/login/?next=%s' % request.path)
    context = {'username': username}
    return render(request, 'betterweb_app/landing.html', context)

@login_required
def deposit(request):
    context = RequestContext(request)
    if request.method == 'POST':
        form = DepositForm(request.POST)
        if form.is_valid():
            deposit = form.save(commit=False)
            deposit.giver = request.user.giver
            deposit.when = datetime.now()
            deposit.save()
            return index(request)
        else:
            print request.POST
            print form.errors
    else:
        form = DepositForm()
        
    return render_to_response('betterweb_app/deposit.html', {'form': form}, context)

@login_required
def withdraw(request):
    return HttpResponse("Hello, %s. You're at the bw withdraw." % username)