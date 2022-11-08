# Generated by Django 4.0.3 on 2022-11-06 08:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Expenses',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.CharField(max_length=8, null=True)),
                ('month', models.CharField(max_length=8, null=True)),
                ('year', models.CharField(max_length=8, null=True)),
                ('option', models.CharField(choices=[('Credit', 'Credit'), ('Debit', 'Debit')], max_length=8, null=True)),
                ('amount', models.CharField(max_length=8, null=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
