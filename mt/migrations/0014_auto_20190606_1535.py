# Generated by Django 2.2 on 2019-06-06 10:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mt', '0013_auto_20190606_1534'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dockeystroke',
            name='trump',
            field=models.CharField(default='N', max_length=1),
        ),
    ]
