# Generated by Django 3.2 on 2023-02-25 16:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freelance_bot', '0007_alter_order_freelancer_message'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='message',
            options={'verbose_name': 'Сообщение', 'verbose_name_plural': 'Сообщения'},
        ),
        migrations.AlterField(
            model_name='order',
            name='file',
            field=models.URLField(blank=True, null=True, verbose_name='Файл'),
        ),
    ]
