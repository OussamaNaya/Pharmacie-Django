# Generated by Django 5.0 on 2023-12-17 02:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pharmacie', '0002_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='eml',
            field=models.EmailField(max_length=254),
        ),
        migrations.AlterField(
            model_name='contact',
            name='fn',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AlterField(
            model_name='contact',
            name='ln',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='contact',
            name='msg',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='contact',
            name='sub',
            field=models.CharField(max_length=255),
        ),
    ]