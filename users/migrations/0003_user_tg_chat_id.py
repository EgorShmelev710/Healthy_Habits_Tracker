# Generated by Django 5.0.7 on 2024-07-24 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_alter_user_options_remove_user_username_user_avatar_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='tg_chat_id',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Телеграм chat-id'),
        ),
    ]
