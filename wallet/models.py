from django.db import models
from django.contrib.auth.models import User

TRANSACTION_TYPES = [
    ('buy', 'Buy'),
    ('sell', 'Sell'),
    ('transfer', 'Transfer'),
]


class AssetType(models.Model):
    name = models.CharField(max_length=16)

    def __str__(self):
        return self.name


class Asset(models.Model):
    ticker = models.CharField(max_length=10)
    name = models.CharField(max_length=64)
    asset_type = models.ManyToManyField(AssetType)

    def __str__(self):
        return self.name


class WalletType(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name


class Wallet(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    wallet_type = models.ForeignKey(
        WalletType, on_delete=models.SET_NULL, null=True)
    assets = models.ManyToManyField(Asset, blank=True)

    def __str__(self):
        return self.user.username


class Transaction(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    asset = models.ForeignKey(Asset, on_delete=models.SET_NULL, null=True)
    quantity = models.DecimalField(max_digits=16, decimal_places=8)
    transaction_type = models.CharField(
        max_length=8, choices=TRANSACTION_TYPES, default='transfer')
    date = models.DateTimeField(auto_now_add=True)
    price = models.DecimalField(max_digits=16, decimal_places=8)
