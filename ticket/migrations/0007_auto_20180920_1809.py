# Generated by Django 2.1.1 on 2018-09-20 10:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticket', '0006_auto_20180920_1757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tickets',
            name='ttimeused',
            field=models.FloatField(null=True, verbose_name='耗时'),
        ),
    ]
