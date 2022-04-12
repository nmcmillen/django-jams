from django.db import models

# Create your models here.
from django.db import models

class Artist(models.Model):
    artist_name = models.CharField(max_length=100)
    music_genre = models.CharField(max_length=50)

    def __str__(self):
        return self.artist_name

class Song(models.Model):
    artist_name = models.ManyToManyField(Artist)
    song_name = models.CharField(max_length=100)
    song_length = models.IntegerField()

    def __str__(self):
        return self.song_name

class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    album_title = models.CharField(max_length=100)
    release_date = models.DateField()
    song = models.ManyToManyField(Song)
    song_amount = models.IntegerField()

    def __str__(self):
        return self.album_title
