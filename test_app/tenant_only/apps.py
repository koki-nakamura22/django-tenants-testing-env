from django.apps import AppConfig


class TenantOnlyConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tenant_only'
