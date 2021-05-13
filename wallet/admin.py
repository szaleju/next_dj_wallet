from django.contrib import admin
from .models import *


class WalletAdmin(admin.ModelAdmin):
    list_display = ['user', 'wallet_type']


class TransactionAdmin(admin.ModelAdmin):
    list_display = ['date', 'asset', 'quantity']


admin.site.register(AssetType)
admin.site.register(Asset)
admin.site.register(WalletType)
admin.site.register(Wallet, WalletAdmin)
admin.site.register(Transaction, TransactionAdmin)
