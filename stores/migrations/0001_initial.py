# Generated by Django 4.1.7 on 2023-03-30 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Carousel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slide', models.ImageField(upload_to='slider')),
                ('created_at', models.DateField(auto_now_add=True)),
            ],
        ),
    ]
