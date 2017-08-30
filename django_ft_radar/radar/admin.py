from django.contrib import admin

from .models import (Category, Source, Tag, LeadStatus,
                     Lead, Industry, Company, CompanyContact)

admin.site.register(Category)
admin.site.register(Source)
admin.site.register(Tag)
admin.site.register(LeadStatus)
admin.site.register(Lead)
admin.site.register(Industry)
admin.site.register(Company)
admin.site.register(CompanyContact)