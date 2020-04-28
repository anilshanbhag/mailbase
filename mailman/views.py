from django.shortcuts import render

# Create your views here.

def index(request):
  ctx = {}
  return render(request, 'mail_app.html', ctx)

def create(request):
  ctx = {}
  return render(request, 'create.html', ctx)

def edit(request):
  ctx = {}
  return render(request, 'mail_edit.html', ctx)

def send_to(request):
  ctx = {}
  return render(request, 'mail_send_to.html', ctx)

def templates(request):
  ctx = {}
  return render(request, 'mail_templates.html', ctx)

def create_template(request):
  ctx = {}
  return render(request, 'mail_create_template.html', ctx)

def edit_template(request):
  ctx = {}
  return render(request, 'mail_edit_template.html', ctx)

def use_template(request):
  ctx = {}
  return render(request, 'mail_app.html', ctx)

def list(request):
  ctx = {}
  return render(request, 'mail_app.html', ctx)

def new_list(request):
  ctx = {}
  return render(request, 'mail_app.html', ctx)

def edit_list(request):
  ctx = {}
  return render(request, 'mail_app.html', ctx)

def subscribers(request):
  ctx = {}
  return render(request, 'mail_app.html', ctx)

def reports(request):
  ctx = {}
  return render(request, 'mail_app.html', ctx)
