# Generated by Django 4.2.2 on 2023-07-30 14:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('AlquilerApp', '0002_alter_alquiler_cod'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alquiler',
            name='cod',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='alquiler',
            name='item',
            field=models.CharField(max_length=60),
        ),
        migrations.AlterField(
            model_name='alquiler',
            name='precio',
            field=models.FloatField(max_length=20),
        ),
        migrations.CreateModel(
            name='Avatar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('imagen', models.ImageField(blank=True, null=True, upload_to='avatares')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
