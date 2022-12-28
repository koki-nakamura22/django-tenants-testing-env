from django.apps import AppConfig


class TenantCommonConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'tenant_common'
