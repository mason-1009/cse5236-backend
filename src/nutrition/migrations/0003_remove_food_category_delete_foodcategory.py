# Generated by Django 4.2.6 on 2023-10-30 21:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('nutrition', '0002_alter_food_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='food',
            name='category',
        ),
        migrations.DeleteModel(
            name='FoodCategory',
        ),
    ]
