from django.contrib import admin

from credit_app.models import Contract, LoanApplication, Producer, Product


class ProducerAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "created_at")
    list_display_links = ("id", "name")
    search_fields = ("name",)


class ProductAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "created_at")
    list_display_links = ("id", "name")
    search_fields = ("name",)


class ContractAdmin(admin.ModelAdmin):
    list_display = ("id", "number", "created_at")
    list_display_links = ("id", "number")
    search_fields = ("number",)


class LoanApplicationAdmin(admin.ModelAdmin):
    list_display = ("id", "number")
    list_display_links = ("id", "number")
    search_fields = ("number",)


admin.site.register(Producer, ProducerAdmin)
admin.site.register(Product, ProducerAdmin)
admin.site.register(Contract, ContractAdmin)
admin.site.register(LoanApplication, LoanApplicationAdmin)
