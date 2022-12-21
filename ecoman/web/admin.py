from django.contrib import admin
from .models import Foydalanuvchi,Post

class PostAdmin(admin.ModelAdmin):
    fields = ( 'foydalanuvchi','image_tag','tasdiq' )
    readonly_fields = ('image_tag',)

admin.site.register(Foydalanuvchi)
admin.site.register(Post,PostAdmin)
