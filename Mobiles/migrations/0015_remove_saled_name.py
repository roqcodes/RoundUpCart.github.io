# Generated by Django 3.2.3 on 2021-05-28 04:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Mobiles', '0014_alter_product_data'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='saled',
            name='name',
        ),
    ]
