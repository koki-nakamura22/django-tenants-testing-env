from django.contrib import admin

from tenant_common.models import Client, Domain


class DomainInline(admin.TabularInline):
    model = Domain


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    inlines = [DomainInline]
    list_display = ('schema_name', 'name')

    def delete_queryset(self, request, queryset):
        for tenant in queryset:
            tenant.auto_drop_schema = True
            tenant.delete()
