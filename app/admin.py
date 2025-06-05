from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Usuario,Ambiente,Historico,Sensor
# Register your models here.
class UsuarioAdmin(UserAdmin):
    fieldsets = UserAdmin.fieldsets + (
        ('Novos campos',{'fields': ('categoria',)}),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        (None,{'fields': ('categoria',)}),
    )

admin.site.register(Usuario)

admin.site.register(Ambiente)
admin.site.register(Historico)
admin.site.register(Sensor)