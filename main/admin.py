"""
This is admin view for main application
"""
from django.contrib import admin

from .models import *

admin.site.register(MyTest)
admin.site.register(Card)
admin.site.register(Result)
admin.site.register(Comments)
