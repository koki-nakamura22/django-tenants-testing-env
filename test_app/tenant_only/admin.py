from django.contrib import admin

from tenant_only.models import Goods


@admin.register(Goods)
class GoodsAdmin(admin.ModelAdmin):
    pass
