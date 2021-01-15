from django.contrib import admin



# Register your models here.

from .models import *

admin.site.register(person)
admin.site.register(post)
admin.site.register(blog)
admin.site.register(following)