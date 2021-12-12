# Generated by Django 3.2.8 on 2021-10-29 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_triund'),
    ]

    operations = [
        migrations.CreateModel(
            name='Kareri',
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
        migrations.AlterField(
            model_name='triund',
            name='person',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='triund',
            name='zip',
            field=models.CharField(max_length=10, null=True),
        ),
    ]
