# Generated by Django 4.0 on 2021-12-08 17:09

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='article',
            options={'ordering': ['-publish'], 'verbose_name': 'مقاله', 'verbose_name_plural': 'مقالات'},
        ),
    ]
