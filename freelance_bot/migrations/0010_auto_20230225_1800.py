# Generated by Django 3.2 on 2023-02-25 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freelance_bot', '0009_alter_order_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='order',
            name='file',
        ),
        migrations.AddField(
            model_name='order',
            name='telegram_file_id',
            field=models.CharField(blank=True, max_length=200, null=True, verbose_name='ID файла в телеграм'),
        ),
    ]