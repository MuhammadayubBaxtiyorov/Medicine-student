# Generated by Django 4.1.2 on 2022-10-13 16:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medtimer_bot', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='telegramchat',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='telegramstate',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='telegramuser',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
