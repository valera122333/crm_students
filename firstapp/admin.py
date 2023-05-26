from django.contrib import admin
from firstapp.models import Post,ListGroups,ListStudents,UserProfileInfo
# Register your models here.
admin.site.register(Post)
admin.site.register(ListGroups)
admin.site.register(ListStudents)
admin.site.register(UserProfileInfo)
