from django.contrib import admin
from request.models import Request, Point

class RequestAdmin(admin.ModelAdmin):
    fieldsets = [
        (None, {'fields': ['source', 'location', 'date', 'time', 'approval', 'lat', 'lng']}),
    ]
    list_display = ('source', 'approval')
    list_filter = ['approval']
    search_fields = ['source']
    readonly_fields = ['source', 'location', 'date', 'time', 'lat', 'lng']
    def has_add_permission(self, request):
        return False
admin.site.register(Request, RequestAdmin)
admin.site.register(Point)