# Generated by Django 3.1.7 on 2021-06-03 13:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ebook_store_app', '0003_auto_20210520_1407'),
    ]

    operations = [
        migrations.AlterField(
            model_name='genre',
            name='genre_type',
            field=models.CharField(max_length=64, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='adress',
            field=models.CharField(blank=True, max_length=80, null=True),
        ),
        migrations.AlterField(
            model_name='publisher',
            name='company_name',
            field=models.CharField(max_length=150, null=True, unique=True),
        ),
        migrations.AlterField(
            model_name='shipping',
            name='adress',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='shipping',
            name='city',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='name',
            field=models.CharField(max_length=64, null=True),
        ),
    ]
