# Generated by Django 4.0 on 2021-12-18 10:53

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('admin', '0003_logentry_add_action_flag_choices'),
        ('blog', '0007_article_is_special_alter_article_status'),
        ('auth', '0012_alter_user_first_name_max_length'),
        ('account', '0006_rename_user_nob'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Nob',
            new_name='User',
        ),
    ]