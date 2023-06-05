from django.contrib import admin
from .models import Pratica, Agente, Magistrato, Indagato

# Register your models here.
admin.site.register(Pratica)
admin.site.register(Agente)
admin.site.register(Magistrato)
admin.site.register(Indagato)