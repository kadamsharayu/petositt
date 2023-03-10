# Generated by Django 4.0.4 on 2022-05-05 09:40

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='PetWalking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pet_detail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pet_walking', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Pets',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pet_type', models.CharField(max_length=256)),
                ('pet_age', models.IntegerField()),
                ('pet_name', models.CharField(max_length=256)),
                ('breed_name', models.CharField(max_length=256)),
                ('pet_weight', models.CharField(max_length=256)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pets', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PetGrooming',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pet_service_type', models.CharField(max_length=256)),
                ('pet_detail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pet_grooming', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PetBoarding',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.TimeField()),
                ('meal', models.CharField(max_length=500)),
                ('special_care', models.TextField()),
                ('pet_detail', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='pet_boarding', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
