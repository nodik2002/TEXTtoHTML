from django.contrib import admin
from .models import Post,Image

class ImageAdmin(admin.ModelAdmin):
    list_display = ['slug']


admin.site.register(Post)
admin.site.register(Image,ImageAdmin)
