from django.contrib import admin
from .models import Event, Category, Location, Attended

class EventAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['event_title', 'event_description', 'event_image', 'event_location', 'event_source', 'event_category']}),
        ('Timings', {'fields': ['event_start_time', 'event_start_date', 'event_end_time', 'event_end_date']}),
        ('Publish', {'fields': ['publishing_location', 'pub_date']})
    ]
    list_display = ('event_title', 'pub_date')
    list_filter = ['event_source']
    search_fields = ['event_title']
admin.site.register(Event, EventAdmin)
admin.site.register(Category)
admin.site.register(Location)
# admin.site.register(Attended)