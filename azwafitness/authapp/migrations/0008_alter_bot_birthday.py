# Generated by Django 4.1.7 on 2023-04-22 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('authapp', '0007_suggest_alter_bot_birthday'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bot',
            name='birthday',
            field=models.DateField(),
        ),
    ]
