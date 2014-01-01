from django.shortcuts import render, redirect, render_to_response
from django.http import HttpResponse
from django.template import RequestContext
from betterweb_app.forms import DepositForm

def index(request):
    return HttpResponse("Hello, world. You're at the bw index.")

def register(request):
    return HttpResponse("Hello, world. You're at the bw register.")

def landing(request, username):
    print request.user.is_authenticated()
    if not request.user.is_authenticated():
        return redirect('/login/?next=%s' % request.path)
    context = {'username': username}
    return render(request, 'betterweb_app/landing.html', context)

def deposit(request, username):
    context = RequestContext(request)
    print request.POST
    if request.method == 'POST':
        form = DepositForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return index(request)
        else:
            print form.errors
    else:
        form = DepositForm()
        
    return render_to_response('betterweb_app/deposit.html', {'form': form}, context)
    #return HttpResponse("Hello, %s. You're at the bw deposit." % username)

def withdraw(request, username):
    return HttpResponse("Hello, %s. You're at the bw withdraw." % username)