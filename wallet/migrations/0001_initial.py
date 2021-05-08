# Generated by Django 3.2.2 on 2021-05-08 08:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Asset',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ticker', models.CharField(max_length=10)),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='AssetType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16)),
            ],
        ),
        migrations.CreateModel(
            name='WalletType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
            ],
        ),
        migrations.CreateModel(
            name='Wallet',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('assets', models.ManyToManyField(to='wallet.Asset')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('wallet_type', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='wallet.wallettype')),
            ],
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('quantity', models.DecimalField(decimal_places=8, max_digits=16)),
                ('transaction_type', models.CharField(choices=[('buy', 'Buy'), ('sell', 'Sell'), ('transfer', 'Transfer')], default='transfer', max_length=8)),
                ('date', models.DateTimeField(auto_now_add=True)),
                ('price', models.DecimalField(decimal_places=8, max_digits=16)),
                ('asset', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='wallet.asset')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='asset',
            name='asset_type',
            field=models.ManyToManyField(to='wallet.AssetType'),
        ),
    ]