# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-04-20 09:01
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):
    atomic = False

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('permabots', '0002_auto_20160414_1051'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bot',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date created')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Date updated')),
                ('name', models.CharField(db_index=True, help_text='Name for the bot', max_length=100, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Bot',
                'verbose_name_plural': 'Bots',
            },
        ),
        migrations.CreateModel(
            name='KikBot',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date created')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Date updated')),
                ('enabled', models.BooleanField(default=True, help_text='Enable/disable telegram bot', verbose_name='Enable')),
                ('api_key', models.CharField(db_index=True, max_length=200, verbose_name='Kik Bot API key')),
                ('username', models.CharField(max_length=200, verbose_name='Kik Bot User name')),
            ],
            options={
                'verbose_name': 'Kik Bot',
                'verbose_name_plural': 'Kik Bots',
            },
        ),
        migrations.CreateModel(
            name='KikChat',
            fields=[
                ('id', models.CharField(max_length=150, primary_key=True, serialize=False, verbose_name='Id')),
            ],
            options={
                'verbose_name': 'Kik Chat',
                'verbose_name_plural': 'Kik Chats',
            },
        ),
        migrations.CreateModel(
            name='KikChatState',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date created')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Date updated')),
                ('context', models.TextField(blank=True, help_text='Context serialized to json when this state was set', null=True, verbose_name='Context')),
                ('chat', models.ForeignKey(help_text='Chat in Kik API format. https://dev.kik.com/#/docs/messaging#authentication', on_delete=django.db.models.deletion.CASCADE, related_name='kik_chatstates', to='permabots.KikChat', verbose_name='Kik Chat')),
            ],
            options={
                'verbose_name': 'Kik Chats States',
            },
        ),
        migrations.CreateModel(
            name='KikMessage',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date created')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Date updated')),
                ('message_id', models.UUIDField(db_index=True, verbose_name='Id')),
                ('timestamp', models.DateTimeField(verbose_name='Timestamp')),
                ('body', models.TextField(blank=True, null=True, verbose_name='Body')),
                ('chat', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='permabots.KikChat', verbose_name='Chat')),
            ],
            options={
                'ordering': ['-timestamp'],
                'verbose_name': 'Kik Message',
                'verbose_name_plural': 'Kik Messages',
            },
        ),
        migrations.CreateModel(
            name='KikRecipient',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Date created')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Date updated')),
                ('chat_id', models.CharField(db_index=True, help_text='Chat identifier provided by Kik API', max_length=150, verbose_name='Chat Id')),
                ('username', models.CharField(db_index=True, max_length=255, verbose_name='User name')),
                ('name', models.CharField(db_index=True, help_text='Name of recipient', max_length=100, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Kik Recipient',
                'verbose_name_plural': 'Kik Recipients',
            },
        ),
        migrations.CreateModel(
            name='KikUser',
            fields=[
                ('username', models.CharField(max_length=255, primary_key=True, serialize=False, verbose_name='User name')),
                ('first_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='First name')),
                ('last_name', models.CharField(blank=True, max_length=255, null=True, verbose_name='Last name')),
            ],
            options={
                'verbose_name': 'Kik User',
                'verbose_name_plural': 'Kik Users',
            },
        ),
        migrations.AlterModelOptions(
            name='telegramchatstate',
            options={'verbose_name': 'Telegram Chats States'},
        ),
        migrations.RemoveField(
            model_name='telegrambot',
            name='owner',
        ),
        migrations.AddField(
            model_name='telegramchatstate',
            name='user',
            field=models.ForeignKey(default=None, help_text='Telegram unique username', on_delete=django.db.models.deletion.CASCADE, related_name='telegram_chatstates', to='permabots.User', verbose_name='Telegram User'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='environmentvar',
            name='bot',
            field=models.ForeignKey(help_text='Bot which variable is attached.', on_delete=django.db.models.deletion.CASCADE, related_name='env_vars', to='permabots.Bot', verbose_name='Bot'),
        ),
        migrations.AlterField(
            model_name='handler',
            name='bot',
            field=models.ForeignKey(help_text='Bot which Handler is attached to', on_delete=django.db.models.deletion.CASCADE, related_name='handlers', to='permabots.Bot', verbose_name='Bot'),
        ),
        migrations.AlterField(
            model_name='hook',
            name='bot',
            field=models.ForeignKey(help_text='Bot which Hook is attached', on_delete=django.db.models.deletion.CASCADE, related_name='hooks', to='permabots.Bot', verbose_name='Bot'),
        ),
        migrations.AlterField(
            model_name='state',
            name='bot',
            field=models.ForeignKey(help_text='Bot which state is attached to', on_delete=django.db.models.deletion.CASCADE, related_name='states', to='permabots.Bot', verbose_name='Bot'),
        ),
        migrations.AlterField(
            model_name='telegrambot',
            name='enabled',
            field=models.BooleanField(default=True, help_text='Enable/disable telegram bot', verbose_name='Enable'),
        ),
        migrations.AlterField(
            model_name='telegrambot',
            name='user_api',
            field=models.OneToOneField(blank=True, help_text='Telegram API info. Automatically retrieved from Telegram', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='telegram_bot', to='permabots.User', verbose_name='Telegram Bot User'),
        ),
        migrations.AlterField(
            model_name='telegramchatstate',
            name='chat',
            field=models.ForeignKey(help_text='Chat in Telegram API format. https://core.telegram.org/bots/api#chat', on_delete=django.db.models.deletion.CASCADE, related_name='telegram_chatstates', to='permabots.Chat', verbose_name='Chat'),
        ),
        migrations.AlterField(
            model_name='telegramchatstate',
            name='state',
            field=models.ForeignKey(help_text='State related to the chat', on_delete=django.db.models.deletion.CASCADE, related_name='telegramchatstate_chat', to='permabots.State', verbose_name='State'),
        ),
        migrations.AlterField(
            model_name='telegramrecipient',
            name='hook',
            field=models.ForeignKey(help_text='Hook which recipient is attached to', on_delete=django.db.models.deletion.CASCADE, related_name='telegram_recipients', to='permabots.Hook', verbose_name='Hook'),
        ),
        migrations.AddField(
            model_name='kikrecipient',
            name='hook',
            field=models.ForeignKey(help_text='Hook which recipient is attached to', on_delete=django.db.models.deletion.CASCADE, related_name='kik_recipients', to='permabots.Hook', verbose_name='Hook'),
        ),
        migrations.AddField(
            model_name='kikmessage',
            name='from_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='permabots.KikUser', verbose_name='User'),
        ),
        migrations.AddField(
            model_name='kikchatstate',
            name='state',
            field=models.ForeignKey(help_text='State related to the chat', on_delete=django.db.models.deletion.CASCADE, related_name='kikchatstate_chat', to='permabots.State', verbose_name='State'),
        ),
        migrations.AddField(
            model_name='kikchatstate',
            name='user',
            field=models.ForeignKey(help_text='Kik unique username', on_delete=django.db.models.deletion.CASCADE, related_name='kik_chatstates', to='permabots.KikUser', verbose_name='Kik User'),
        ),
        migrations.AddField(
            model_name='kikchat',
            name='participants',
            field=models.ManyToManyField(blank=True, related_name='chats', to='permabots.KikUser', verbose_name='Participants'),
        ),
        migrations.AddField(
            model_name='bot',
            name='kik_bot',
            field=models.OneToOneField(blank=True, help_text='Kik Bot', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bot', to='permabots.KikBot', verbose_name='Kik Bot'),
        ),
        migrations.AddField(
            model_name='bot',
            name='owner',
            field=models.ForeignKey(help_text='User who owns the bot', on_delete=django.db.models.deletion.CASCADE, related_name='bots', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='bot',
            name='telegram_bot',
            field=models.OneToOneField(blank=True, help_text='Telegram Bot', null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bot', to='permabots.TelegramBot', verbose_name='Telegram Bot'),
        ),
        migrations.AlterUniqueTogether(
            name='kikmessage',
            unique_together=set([('message_id', 'chat')]),
        ),
        migrations.AlterUniqueTogether(
            name='kikchatstate',
            unique_together=set([('chat', 'user')]),
        ),
    ]
