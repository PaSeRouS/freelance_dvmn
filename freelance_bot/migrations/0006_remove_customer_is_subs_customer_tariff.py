# Generated by Django 4.0.5 on 2023-02-24 19:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('freelance_bot', '0005_customer_is_subs_customer_telegram_id_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='is_subs',
        ),
        migrations.AddField(
            model_name='customer',
            name='tariff',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='freelance_bot.tariff', verbose_name='Подписка'),
        ),
    ]
