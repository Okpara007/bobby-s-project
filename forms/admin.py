from django.contrib import admin

# Register your models here.
from .models import Feedback
class FeedbackAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email', 'department', 'level', 'meal', 'rating')
    list_display_links = ('id', 'meal', 'rating')
    list_filter = ('meal', 'rating')
    search_fields = ('meal', 'rating')
    list_per_page = 50

admin.site.register(Feedback, FeedbackAdmin)
