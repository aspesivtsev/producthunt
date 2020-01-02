# Generated by Django 3.0 on 2019-12-29 14:39

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('products', '0002_auto_20191229_1523'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='hunter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='product',
            name='votes_total',
            field=models.IntegerField(default=1),
        ),
    ]
