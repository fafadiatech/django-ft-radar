from django.contrib import admin

from .models import (Category, Source, Tag, LeadStatus, Lead)

admin.site.register(Category)
admin.site.register(Source)
admin.site.register(Tag)
admin.site.register(LeadStatus)
admin.site.register(Lead)
