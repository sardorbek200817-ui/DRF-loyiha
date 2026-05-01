from django.contrib import admin
from .models import User_profile , News , Author , Category , Likes

admin.site.register(User_profile)
admin.site.register(Likes)
admin.site.register(News)
admin.site.register(Author)
admin.site.register(Category)
