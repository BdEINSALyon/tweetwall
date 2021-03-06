# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2017-03-03 08:50
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0003_auto_20170227_2337'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='feed',
            options={'verbose_name': 'flux', 'verbose_name_plural': 'flux'},
        ),
        migrations.AlterModelOptions(
            name='message',
            options={'verbose_name': 'message'},
        ),
        migrations.AlterModelOptions(
            name='provider',
            options={'verbose_name': 'Fournisseur'},
        ),
        migrations.AlterField(
            model_name='feed',
            name='hashtag',
            field=models.CharField(max_length=50, verbose_name='hashtag'),
        ),
        migrations.AlterField(
            model_name='feed',
            name='providers',
            field=models.ManyToManyField(related_name='feeds', to='social.Provider', verbose_name='fournisseurs'),
        ),
        migrations.AlterField(
            model_name='message',
            name='author_name',
            field=models.CharField(blank=True, max_length=50, verbose_name="nom de l'auteur"),
        ),
        migrations.AlterField(
            model_name='message',
            name='author_picture',
            field=models.URLField(blank=True, max_length=300, verbose_name="image de l'auteur"),
        ),
        migrations.AlterField(
            model_name='message',
            name='author_username',
            field=models.CharField(max_length=50, verbose_name="nom d'utilisateur de l'auteur"),
        ),
        migrations.AlterField(
            model_name='message',
            name='feed',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='social.Feed', verbose_name='flux'),
        ),
        migrations.AlterField(
            model_name='message',
            name='image',
            field=models.URLField(blank=True, max_length=300, verbose_name='image'),
        ),
        migrations.AlterField(
            model_name='message',
            name='provider',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='messages', to='social.Provider', verbose_name='fournisseur'),
        ),
        migrations.AlterField(
            model_name='message',
            name='provider_post_id',
            field=models.CharField(max_length=200, verbose_name='identifiant du post chez le fournisseur'),
        ),
        migrations.AlterField(
            model_name='message',
            name='published_at',
            field=models.DateTimeField(verbose_name='publié le'),
        ),
        migrations.AlterField(
            model_name='message',
            name='status',
            field=models.CharField(choices=[('PE', 'En attente'), ('PU', 'Publié'), ('PR', 'Promu'), ('RE', 'Rejeté')], default='PE', max_length=2, verbose_name='statut'),
        ),
        migrations.AlterField(
            model_name='message',
            name='text',
            field=models.TextField(blank=True, verbose_name='texte'),
        ),
        migrations.AlterField(
            model_name='message',
            name='validated_at',
            field=models.DateTimeField(blank=True, null=True, verbose_name='validé le'),
        ),
        migrations.AlterField(
            model_name='message',
            name='video',
            field=models.URLField(blank=True, max_length=300, verbose_name='vidéo'),
        ),
        migrations.AlterField(
            model_name='message',
            name='video_is_gif',
            field=models.BooleanField(default=False, verbose_name='la vidéo est un GIF'),
        ),
        migrations.AlterField(
            model_name='provider',
            name='app_id',
            field=models.CharField(max_length=100, verbose_name="identifiant de l'application"),
        ),
        migrations.AlterField(
            model_name='provider',
            name='app_secret',
            field=models.CharField(max_length=200, verbose_name="secret de l'application"),
        ),
        migrations.AlterField(
            model_name='provider',
            name='name',
            field=models.CharField(max_length=50, verbose_name='nom'),
        ),
        migrations.AlterField(
            model_name='provider',
            name='type',
            field=models.CharField(choices=[('TWI', 'Twitter'), ('INS', 'Instagram')], max_length=3, verbose_name='type'),
        ),
    ]
