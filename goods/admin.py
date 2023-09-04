from django.contrib import admin

from goods.models import Contact, Good, Supplier, RetailNetwork


@admin.action(description="Очистить задолженность перед поставщиком")
def accounts_receivable_reset(modeladmin, request, queryset):
    queryset.update(accounts_receivable=0)


class LinkAdmin(admin.ModelAdmin):

    list_display = ('title', 'supplier', 'contact', 'good', 'accounts_receivable', 'created')
    list_display_links = ('title', 'supplier', 'accounts_receivable',)
    list_filter = ('contact__city',)
    search_fields = ('contact__city',)
    actions = (accounts_receivable_reset,)


admin.site.register(RetailNetwork, LinkAdmin)
admin.site.register(Supplier)
admin.site.register(Good)
admin.site.register(Contact)
