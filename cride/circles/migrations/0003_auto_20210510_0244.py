# Generated by Django 3.1.1 on 2021-05-10 02:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('circles', '0002_auto_20210506_0942'),
    ]

    operations = [
        migrations.RenameField(
            model_name='membership',
            old_name='remaining_invitation',
            new_name='remaining_invitations',
        ),
    ]
