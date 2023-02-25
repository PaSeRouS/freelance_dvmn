# Generated by Django 3.2 on 2023-02-25 16:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freelance_bot', '0008_auto_20230225_1613'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='status',
            field=models.CharField(choices=[('create', 'Создан'), ('work', 'В работе'), ('closed', 'Завершен')], db_index=True, default='create', max_length=20, verbose_name='Статус заказа'),
        ),
    ]
