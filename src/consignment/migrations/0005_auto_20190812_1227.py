# Generated by Django 2.2.2 on 2019-08-12 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('consignment', '0004_auto_20190812_1226'),
    ]

    operations = [
        migrations.AlterField(
            model_name='office',
            name='office_pincode',
            field=models.IntegerField(choices=[(481001, 'Balaghat (BGT)')]),
        ),
    ]
