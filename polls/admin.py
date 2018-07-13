from django.contrib import admin
from polls.models import Choice, Poll, Voted
from events.models import Location

class ChoiceInline(admin.TabularInline):
    model = Choice
    readonly_fields = ['choice_count']
    extra = 2

class PollAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['poll_title', 'poll_description', 'poll_image', 'poll_source']}),
        ('Deadline', {'fields': ['poll_deadline']}),
        ('Publish', {'fields': ['publishing_location', 'pub_date']})
    ]
    inlines = [ChoiceInline]
    list_display = ('poll_title', 'pub_date')
    list_filter = ['poll_source']
    search_fields = ['poll_title']
admin.site.register(Poll, PollAdmin)