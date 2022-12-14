# Generated by Django 4.0.1 on 2022-12-12 18:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('goals', '0005_alter_goalcategory_board'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goal',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='goals.goalcategory', verbose_name='Категория'),
        ),
        migrations.AlterField(
            model_name='goal',
            name='description',
            field=models.TextField(blank=True, default=None, null=True, verbose_name='Описание'),
        ),
        migrations.AlterField(
            model_name='goal',
            name='due_date',
            field=models.DateField(blank=True, default=None, null=True, verbose_name='Дата выполнения'),
        ),
        migrations.AlterField(
            model_name='goal',
            name='title',
            field=models.CharField(max_length=255, verbose_name='Заголовок'),
        ),
        migrations.AlterField(
            model_name='goal',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='goals', to=settings.AUTH_USER_MODEL, verbose_name='Пользователь'),
        ),
    ]
