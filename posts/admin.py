from django.contrib import admin
from .models import Post
# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_display= ['__str__','user','timestamp']
    search_fields=['user__username','user__email']
    class Meta:
        model = Post
admin.site.register(Post)