# Generated by Django 3.0.5 on 2020-04-27 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('info', '0002_auto_20200427_1827'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hotel',
            name='star',
            field=models.DecimalField(decimal_places=0, default=1, max_digits=5),
        ),
    ]
