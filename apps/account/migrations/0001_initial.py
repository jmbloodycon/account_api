# Generated by Django 3.1.1 on 2020-09-04 10:13

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Account',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('account_id', models.UUIDField(default=uuid.uuid4, editable=False, unique=True, verbose_name='Account id')),
                ('full_name', models.CharField(max_length=255, verbose_name='Username')),
                ('current_balance', models.IntegerField(default=0, verbose_name='Current balance')),
                ('hold', models.IntegerField(default=0, verbose_name='Holds')),
                ('status', models.BooleanField(default=True, verbose_name='Is active')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date of creation')),
            ],
            options={
                'verbose_name': 'Account',
                'ordering': ('-created_at',),
            },
        ),
    ]
