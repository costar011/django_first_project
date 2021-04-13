from django.contrib import admin
from . import models


# admin 에 postmodel 을 생성해주겠다.
@admin.register(models.PostModel)
class PostAdmin(admin.ModelAdmin):
    pass
