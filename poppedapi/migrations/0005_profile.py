# Generated by Django 4.1.5 on 2023-01-24 01:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('poppedapi', '0004_delete_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poppedapi.user')),
                ('user_genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='poppedapi.user_genre')),
            ],
        ),
    ]