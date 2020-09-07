# Generated by Django 3.0.3 on 2020-09-07 08:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Board',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('type', models.IntegerField()),
                ('author', models.IntegerField()),
                ('title', models.CharField(max_length=300)),
                ('content', models.CharField(max_length=1500)),
                ('reg_time', models.DateTimeField(auto_now=True)),
                ('update_time', models.DateTimeField(null=True)),
            ],
            options={
                'db_table': 'Board',
            },
        ),
    ]
