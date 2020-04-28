from django.views.generic.base import TemplateView
from django.shortcuts import redirect, render
from django.http import Http404, HttpResponse
from django.conf import settings

def index(request):
  ctx = {}

  if not request.user.is_authenticated:
    return redirect('/accounts/login/')
  else:
    return redirect('/mailman/')
