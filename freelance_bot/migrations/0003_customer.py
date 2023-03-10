# Generated by Django 4.0.5 on 2023-02-22 13:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('freelance_bot', '0002_input_tariffs'),
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, max_length=20, verbose_name='Имя')),
                ('last_name', models.CharField(blank=True, max_length=20, verbose_name='Фамилия')),
                ('nickname', models.CharField(db_index=True, max_length=30, verbose_name='Никнейм в телеграме')),
                ('is_freelancer', models.BooleanField(default=False, verbose_name='Фрилансер')),
            ],
        ),
    ]
