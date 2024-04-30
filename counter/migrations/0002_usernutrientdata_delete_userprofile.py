# Generated by Django 4.1.12 on 2024-04-29 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('counter', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UserNutrientData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=100)),
                ('carbohydrates_total_g', models.FloatField(default=0)),
                ('cholesterol_mg', models.FloatField(default=0)),
                ('fat_saturated_g', models.FloatField(default=0)),
                ('fat_total_g', models.FloatField(default=0)),
                ('fiber_g', models.FloatField(default=0)),
                ('potassium_mg', models.FloatField(default=0)),
                ('protein_g', models.FloatField(default=0)),
                ('sodium_mg', models.FloatField(default=0)),
                ('sugar_g', models.FloatField(default=0)),
            ],
        ),
        migrations.DeleteModel(
            name='UserProfile',
        ),
    ]
