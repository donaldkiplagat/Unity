from django.contrib import admin
from .models import countries,categories,platforms,Game,Profile,News,Comment


class GameAdmin(admin.ModelAdmin):
    filter_horizontal =('platforms','categories')

# Register your models here.
admin.site.register(countries)
admin.site.register(categories)
admin.site.register(platforms)
admin.site.register(Game,GameAdmin)
admin.site.register(Profile)
admin.site.register(News)
admin.site.register(Comment)
