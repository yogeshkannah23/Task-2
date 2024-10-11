from django.contrib import admin
from recipe.models import *
# Register your models here.


admin.site.register(User)
admin.site.register(Category)
admin.site.register(Recipes)
