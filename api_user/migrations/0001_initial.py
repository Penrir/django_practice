# Generated by Django 3.1.1 on 2020-09-07 02:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=128)),
                ('password', models.CharField(max_length=128)),
                ('email', models.EmailField(max_length=256)),
                ('phone', models.CharField(max_length=128, null=True)),
                ('address', models.CharField(max_length=256, null=True)),
                ('join_date', models.DateTimeField(auto_now=True)),
            ],
            options={
                'db_table': 'User',
            },
        ),
    ]