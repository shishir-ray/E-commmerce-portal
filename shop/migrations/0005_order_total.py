# Generated by Django 3.1.1 on 2020-11-30 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0004_auto_20201130_1904'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='total',
            field=models.CharField(default=1, max_length=200),
            preserve_default=False,
        ),
    ]
