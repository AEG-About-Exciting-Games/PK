# Generated by Django 4.2 on 2024-09-12 22:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diaries', '0002_diary_cinema_diary_loc_x_diary_loc_y'),
    ]

    operations = [
        migrations.AlterField(
            model_name='diary',
            name='loc_x',
            field=models.DecimalField(decimal_places=4, max_digits=8),
        ),
        migrations.AlterField(
            model_name='diary',
            name='loc_y',
            field=models.DecimalField(decimal_places=4, max_digits=8),
        ),
    ]
