# Generated by Django 5.0.4 on 2024-04-12 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('aiwriter', '0008_react_magics'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='react',
            name='magics',
        ),
        migrations.AddField(
            model_name='react',
            name='antiheroes',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='react',
            name='leadership',
            field=models.CharField(choices=[('Monarchy', 'Monarchy'), ('Democracy', 'Democracy'), ('Anarchy', 'Anarchy'), ('Dictatorship', 'Dictatorship'), ('Managed Democracy', 'Managed Democracy')], default='Monarchy', max_length=30),
        ),
        migrations.AddField(
            model_name='react',
            name='magic',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='react',
            name='name',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='react',
            name='place',
            field=models.CharField(default='', max_length=30),
        ),
        migrations.AddField(
            model_name='react',
            name='science',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='react',
            name='seas',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='react',
            name='side_characters',
            field=models.CharField(choices=[('0', '0'), ('1', '1'), ('2', '2'), ('4', '4')], default='0', max_length=1),
        ),
        migrations.AddField(
            model_name='react',
            name='stars',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='react',
            name='era',
            field=models.CharField(choices=[('Past', 'Past'), ('Present', 'Present'), ('Future', 'Future'), ('Urban', 'Urban'), ('Prehistoric', 'Prehistoric'), ('Medieval', 'Medieval')], default='', max_length=15),
        ),
    ]
