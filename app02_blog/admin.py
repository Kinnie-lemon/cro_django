from django.contrib import admin
from app02_blog import models
# Register your models here.

admin.site.register(models.UserInfo)
admin.site.register(models.Blog)
admin.site.register(models.Category)
admin.site.register(models.Tags)
admin.site.register(models.Article)
admin.site.register(models.Atcl2Tags)
admin.site.register(models.upanddown)
admin.site.register(models.Comment)