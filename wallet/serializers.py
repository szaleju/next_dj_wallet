from django.contrib.auth.models import User
from .models import *
from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email']


class TransactionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction
        fields = '__all__'


class AssetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Asset
        fields = '__all__'


class WalletSerializer(serializers.ModelSerializer):
    assets = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Wallet
        fields = '__all__'

    def get_assets(self, obj):
        assets = obj.assets.all()
        serializer = AssetSerializer(assets, many=True)
        return serializer.data
