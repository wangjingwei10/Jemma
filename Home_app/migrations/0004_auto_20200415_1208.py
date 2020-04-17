# Generated by Django 3.0.5 on 2020-04-15 12:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Home_app', '0003_auto_20200415_1148'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificate',
            name='ExpireDate',
            field=models.DateField(default='1999-1-1'),
        ),
        migrations.AddField(
            model_name='certificate',
            name='Price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=4),
        ),
        migrations.AddField(
            model_name='customer',
            name='Email',
            field=models.EmailField(default='xxx@xxx.xxx', max_length=254),
        ),
        migrations.AddField(
            model_name='order',
            name='OrderDate',
            field=models.DateField(default='1999-1-1'),
        ),
        migrations.AddField(
            model_name='rating',
            name='Points',
            field=models.IntegerField(default=5),
        ),
        migrations.AddField(
            model_name='tradie',
            name='Email',
            field=models.EmailField(default='xxx@xxx.xxx', max_length=254),
        ),
        migrations.AddField(
            model_name='tradie',
            name='TravelDistance',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=4),
        ),
    ]