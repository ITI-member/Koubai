# Generated by Django 4.0.6 on 2022-09-02 00:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('buy', '0002_remove_listofpurchases_order_plan'),
    ]

    operations = [
        migrations.AddField(
            model_name='listofpurchases',
            name='order_plan',
            field=models.DateField(blank=True, null=True, verbose_name='注文予定日'),
        ),
    ]
