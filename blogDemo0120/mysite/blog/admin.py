#-*- coding: UTF-8 -*-
from django.contrib import admin

from .models import BlogPost,BlogPostAdmin,User


admin.site.register(BlogPost,BlogPostAdmin)


admin.site.register(User)


