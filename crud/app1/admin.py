from django.contrib import admin
from .models import Article, Task
# Register your models here.


class AdminArticle(admin.ModelAdmin):
    list_display = ('id', 'title', 'author', 'email','datetime')


class AdminTask(admin.ModelAdmin):
    list_display = ('id', 'title', 'completed')


admin.site.register(Article,AdminArticle)
admin.site.register(Task,AdminTask)
