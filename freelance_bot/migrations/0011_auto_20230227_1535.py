# Generated by Django 3.2 on 2023-02-27 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('freelance_bot', '0010_auto_20230225_1800'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='message',
            name='chat_id',
        ),
        migrations.AddField(
            model_name='message',
            name='order',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='chat_messages', to='freelance_bot.order', verbose_name='Заказ'),
            preserve_default=False,
        ),
    ]
