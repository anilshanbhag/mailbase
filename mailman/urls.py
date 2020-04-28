from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url
from .views import *

urlpatterns = [
    url(r'^$', index, name='mailman_home'),

    url(r'^create$', create, name='mailman_create'),
    url(r'^save-campaign/$', save_campaign, name='mailman_create'),
    url(r'^edit$', edit, name='mailman_home'),
    url(r'^send-to$', send_to, name='mailman_home'),

    url(r'^templates$', templates, name='mailman_home'),
    url(r'^create-template$', create_template, name='mailman_home'),
    url(r'^edit-template$', edit_template, name='mailman_home'),
    url(r'^template-preview$', create_template, name='mailman_home'),
    url(r'^use-template$', use_template, name='mailman_home'),

    url(r'^list$', list, name='mailman_home'),
    url(r'^new-list$', new_list, name='mailman_home'),
    url(r'^edit-list$', edit_list, name='mailman_home'),

    url(r'^subscribers$', subscribers, name='mailman_home'),

    url(r'^reports$', reports, name='mailman_home'),
]
