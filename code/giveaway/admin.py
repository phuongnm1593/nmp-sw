from django.contrib import admin

from .models import Roll, Hero, Candidate, SessionKey

admin.site.register(Roll)
admin.site.register(Hero)
admin.site.register(Candidate)
admin.site.register(SessionKey)