# Generated by Django 5.0.6 on 2024-06-12 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hawk', '0004_rename_eventsupdates_updates'),
    ]

    operations = [
        migrations.CreateModel(
            name='Athlete',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('picture', models.ImageField(upload_to='athlete_pictures/')),
                ('bio', models.TextField()),
            ],
        ),
    ]