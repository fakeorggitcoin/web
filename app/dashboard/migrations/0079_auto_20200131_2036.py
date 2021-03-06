# Generated by Django 2.2.4 on 2020-01-31 20:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0078_profile_as_representation'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='dont_autofollow_earnings',
            field=models.BooleanField(default=False, help_text='If this option is chosen, Gitcoin will not auto-follow users you do business with'),
        ),
        migrations.AddField(
            model_name='tribemember',
            name='why',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
