from django.contrib import admin
from .models import ServiceAPILog

@admin.register(ServiceAPILog)
class ServiceAPILogAdmin(admin.ModelAdmin):
    list_display = (
        'id',
        'endpoint',
        'service_name',
        'ok',
        'status_code',
        "updated_on",
        "created_on"
    )
    list_filter = ('ok', 'service_name', 'status_code')
    search_fields = ('endpoint', 'service_name',)
    fieldsets = (
        (None, {
            'fields': (
                'endpoint',
                'service_name',
                'ok',
                'status_code',
                'request_data',
                'response_data',
            )
        }),
    )
