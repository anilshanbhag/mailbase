from django.contrib import admin
from .models import *

# Register your models here.
class CampaignAdmin(admin.ModelAdmin):
  list_display = ('from_name', 'from_email', 'title',)

class ListAdmin(admin.ModelAdmin):
  list_display = ('name',)

class LinkAdmin(admin.ModelAdmin):
  list_display = ('campaign', 'link',)

class SubscriberAdmin(admin.ModelAdmin):
  list_display = ('user', 'list', 'unsubscribed', 'bounced')

class TemplateAdmin(admin.ModelAdmin):
  list_display = ('template_name',)

admin.site.register(Campaign, CampaignAdmin)
admin.site.register(List, ListAdmin)
admin.site.register(Link, LinkAdmin)
admin.site.register(Subscriber, SubscriberAdmin)
admin.site.register(Template, TemplateAdmin)
