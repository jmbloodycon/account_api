from django.contrib import admin

from .models import Account


@admin.register(Account)
class ReactionAdmin(admin.ModelAdmin):
    search_fields = (
        'full_name',
    )
    list_display = (
        'account_id',
        'full_name',
        'current_balance',
        'hold',
        'status',
    )
