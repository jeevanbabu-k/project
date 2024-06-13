# Generated by Django 5.0.6 on 2024-06-06 14:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hawk', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='News',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('news_image', models.ImageField(upload_to='news_image/')),
            ],
        ),
    ]