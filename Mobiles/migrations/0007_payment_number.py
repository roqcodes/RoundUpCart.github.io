# Generated by Django 3.2.3 on 2021-05-24 16:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Mobiles', '0006_auto_20210524_2136'),
    ]

    operations = [
        migrations.AddField(
            model_name='payment',
            name='number',
            field=models.IntegerField(default=0),
        ),
    ]
