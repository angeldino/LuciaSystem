# Generated by Django 5.0.3 on 2024-04-05 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0004_supplier_convenio'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='position',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]