# Generated by Django 5.0.3 on 2024-04-02 21:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('user_id', models.IntegerField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
                ('ap_pat', models.CharField(blank=True, max_length=50, null=True)),
                ('ap_mat', models.CharField(blank=True, max_length=50, null=True)),
                ('email', models.EmailField(blank=True, max_length=50, null=True)),
                ('rebe_user', models.CharField(blank=True, max_length=50, null=True)),
                ('pc_user', models.CharField(blank=True, max_length=50, null=True)),
                ('shift', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
    ]