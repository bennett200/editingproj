from django.contrib import admin
from .models import Letter
# Register your models here.

class LetterAdmin(admin.ModelAdmin):
    list_display = ('submitted', 'send_to', 'title', 'first_name', 'last_name')
    list_filter = ('submitted', 'title')
    readonly_fields = ('submitted',)
    fieldsets = (
        (None, {
            'fields': ('send_to', 'title', 'submitted', 'first_name', 'last_name')
        }),
        ('Content and Ending', {
            'classes': ('collapse', ),
            'fields': ('content', 'ending')
        }),
    )

admin.site.register(Letter, LetterAdmin)
