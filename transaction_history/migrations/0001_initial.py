# Generated by Django 5.0.4 on 2024-04-16 11:54

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('store', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='TransactionHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount_uzs', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('amount_usd', models.DecimalField(blank=True, decimal_places=2, max_digits=9, null=True)),
                ('info', models.TextField(blank=True, max_length=1000, null=True)),
                ('type', models.CharField(choices=[('ADD', 'Addition'), ('SUB', 'Subtraction')], default='ADD', max_length=3)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('store', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='transaction_histories', to='store.store')),
            ],
            options={
                'verbose_name_plural': 'Transaction Histories',
                'ordering': ['-created'],
                'indexes': [models.Index(fields=['-created'], name='transaction_created_d9af50_idx')],
            },
        ),
    ]