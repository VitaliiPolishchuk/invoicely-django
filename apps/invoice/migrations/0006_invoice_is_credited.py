# Generated by Django 4.0.4 on 2022-04-16 06:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('invoice', '0005_invoice_bankaccount'),
    ]

    operations = [
        migrations.AddField(
            model_name='invoice',
            name='is_credited',
            field=models.BooleanField(default=False),
        ),
    ]
