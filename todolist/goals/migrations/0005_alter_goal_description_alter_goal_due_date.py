# Generated by Django 4.0.1 on 2022-12-07 13:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goals', '0004_alter_goal_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='goal',
            name='due_date',
            field=models.DateField(verbose_name='Дата выполнения'),
        ),
    ]