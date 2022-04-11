from django.db import models

# Create your models here.
from django.db import models


# class Question(models.Model):
#     question_text = models.CharField(max_length=200)
#     pub_date = models.DateTimeField('date published')

class Artist(models.Model):
    artist_name = models.CharField(max_length=100)
    music_genre = models.CharField(max_length=50)

    def __str__(self):
        return self.artist_name


# class Choice(models.Model):
#     question = models.ForeignKey(Question, on_delete=models.CASCADE)
#     choice_text = models.CharField(max_length=200)
#     votes = models.IntegerField(default=0)

class Song(models.Model):
    artist_name = models.ForeignKey(Artist, on_delete=models.CASCADE)
    song_name = models.CharField(max_length=100)
    song_length = models.IntegerField()

class Album(models.Model):
    artist = models.ForeignKey(Artist, on_delete=models.CASCADE)
    album_title = models.CharField(max_length=100)
    release_date = models.DateTimeField()
    song = models.ForeignKey(Song, on_delete=models.CASCADE)
    song_amount = models.IntegerField()

