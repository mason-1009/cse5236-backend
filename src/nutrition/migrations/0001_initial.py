# Generated by Django 4.2.6 on 2023-10-30 14:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Food',
            fields=[
                ('fdc_id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('data_type', models.CharField(max_length=64)),
                ('description', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='FoodCategory',
            fields=[
                ('category_id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('code', models.CharField(max_length=12, unique=True)),
                ('name', models.CharField(max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='NutrientType',
            fields=[
                ('nutrient_id', models.IntegerField(primary_key=True, serialize=False, unique=True)),
                ('name', models.CharField(max_length=128)),
                ('unit_name', models.CharField(max_length=12)),
            ],
        ),
        migrations.CreateModel(
            name='FoodNutrient',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.DecimalField(decimal_places=2, max_digits=12)),
                ('food', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nutrients', to='nutrition.food')),
                ('nutrient_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='nutrients', to='nutrition.nutrienttype')),
            ],
        ),
        migrations.AddField(
            model_name='food',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='foods', to='nutrition.foodcategory'),
        ),
    ]
