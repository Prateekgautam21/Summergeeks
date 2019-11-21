# Generated by Django 2.2.7 on 2019-11-22 00:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('geekapp', '0007_auto_20191122_0010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='host',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='checkin',
            field=models.DateTimeField(blank=True),
        ),
        migrations.AlterField(
            model_name='visitor',
            name='checkout',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
