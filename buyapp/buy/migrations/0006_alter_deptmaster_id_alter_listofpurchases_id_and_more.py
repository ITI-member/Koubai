# Generated by Django 4.0.7 on 2022-09-14 00:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buy', '0005_auto_20220913_1657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deptmaster',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='listofpurchases',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
        migrations.AlterField(
            model_name='purchasermaster',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
