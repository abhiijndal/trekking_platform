# Generated by Django 3.2.8 on 2021-11-04 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0007_rising'),
    ]

    operations = [
        migrations.CreateModel(
            name='Laka',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('phone', models.CharField(max_length=10)),
                ('email', models.CharField(max_length=50)),
                ('person', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('zip', models.CharField(max_length=10, null=True)),
                ('date', models.CharField(max_length=10)),
            ],
        ),
    ]
