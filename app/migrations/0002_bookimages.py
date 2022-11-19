# Generated by Django 4.1.2 on 2022-11-19 15:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BookImages',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, default='', null=True, upload_to='img')),
                ('book', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='app.book')),
            ],
        ),
    ]
