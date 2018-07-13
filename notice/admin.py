from django.contrib import admin
from notice.models import Notice
from events.models import Location

class NoticeAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['notice_title', 'notice_description', 'notice_image', 'notice_source']}),
        ('Publish', {'fields': ['publishing_location', 'publishing_date']})
    ]
    list_display = ('notice_title', 'publishing_date')
    list_filter = ['notice_source']
    search_fields = ['notice_title']
admin.site.register(Notice, NoticeAdmin)