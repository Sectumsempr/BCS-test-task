# Generated by Django 3.1.5 on 2021-02-02 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_blocks', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='block',
            options={'managed': True, 'verbose_name': 'Блок', 'verbose_name_plural': 'Блоки'},
        ),
        migrations.AlterField(
            model_name='block',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
    ]
