# Generated by Django 5.0 on 2024-01-15 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='movie',
            old_name='download',
            new_name='file',
        ),
        migrations.RenameField(
            model_name='movie',
            old_name='janr',
            new_name='genre',
        ),
        migrations.RemoveField(
            model_name='movie',
            name='tags',
        ),
        migrations.AddField(
            model_name='movie',
            name='description',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='movie',
            name='duration',
            field=models.PositiveSmallIntegerField(),
        ),
    ]
