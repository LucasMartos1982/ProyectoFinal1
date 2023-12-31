# Generated by Django 4.2.2 on 2023-07-24 23:47

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('EstenopoApp', '0002_rename_aerea1_aerea_aerea_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='aerea',
            old_name='aerea',
            new_name='nombre_aerea',
        ),
        migrations.RenameField(
            model_name='aerea',
            old_name='precioaerea',
            new_name='precio_aerea',
        ),
        migrations.RenameField(
            model_name='moda',
            old_name='moda',
            new_name='nombre_moda',
        ),
        migrations.RenameField(
            model_name='moda',
            old_name='preciomoda',
            new_name='precio_moda',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='prod',
            new_name='nombre_prod',
        ),
        migrations.RenameField(
            model_name='producto',
            old_name='precioprod',
            new_name='precio_prod',
        ),
        migrations.RenameField(
            model_name='social',
            old_name='social',
            new_name='nombre_social',
        ),
        migrations.RenameField(
            model_name='social',
            old_name='preciosocial',
            new_name='precio_social',
        ),
    ]
