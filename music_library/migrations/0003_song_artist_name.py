# Generated by Django 4.0.4 on 2022-04-12 18:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('music_library', '0002_remove_song_artist_name_alter_album_release_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='artist_name',
            field=models.ManyToManyField(to='music_library.artist'),
        ),
    ]
