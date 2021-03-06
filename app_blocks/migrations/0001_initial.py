# Generated by Django 3.1.5 on 2021-02-02 13:17

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Block',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('height', models.IntegerField(verbose_name='высота блока')),
                ('hash', models.TextField(verbose_name='хэш блока')),
                ('timestamp', models.IntegerField(verbose_name='время блока')),
                ('miner', models.TextField(verbose_name='адрес майнера')),
                ('transactions_count', models.IntegerField(verbose_name='кол-во транзакций в блоке')),
                ('date', models.DateField(auto_now_add=True)),
            ],
            options={
                'managed': True,
            },
        ),
    ]
