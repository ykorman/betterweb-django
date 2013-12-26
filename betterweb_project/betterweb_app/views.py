from django.shortcuts import render, redirect

from django.http import HttpResponse

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
    return HttpResponse("Hello, %s. You're at the bw deposit." % username)

def withdraw(request, username):
    return HttpResponse("Hello, %s. You're at the bw withdraw." % username)