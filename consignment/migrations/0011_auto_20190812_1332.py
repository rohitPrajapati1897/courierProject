# Generated by Django 2.2.2 on 2019-08-12 08:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('consignment', '0010_deliveryprogress'),
    ]

    operations = [
        migrations.CreateModel(
            name='Transporter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='deliveryprogress',
            name='transporter',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='consignment.Transporter'),
        ),
    ]
