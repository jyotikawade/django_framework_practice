from django.db import models


class Album(models.Model):
    artist = models.CharField(max_length=250)  # hech  sagle variable nanttr column name bananar ahe
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    album_logo = models.CharField(max_length=1500)

    def __str__(self):  # databse shell madhe Album.object.all() mhnlyavr ky disl pahije te ithun tharnar
        return self.album_title + ' - ' + self.artist


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)
    song_title = models.CharField(max_length=250)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):  # databse shell madhe Song.object.all() mhnlyavr ky disl pahije te ithun tharnar
        return self.song_title
