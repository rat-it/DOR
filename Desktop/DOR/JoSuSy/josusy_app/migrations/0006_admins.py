# Generated by Django 2.1.7 on 2019-05-10 12:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('josusy_app', '0005_auto_20190508_1701'),
    ]

    operations = [
        migrations.CreateModel(
            name='Admins',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('password', models.CharField(max_length=100)),
            ],
        ),
    ]
