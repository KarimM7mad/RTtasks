from django.db import models
from django.core.urlresolvers import reverse


class Album(models.Model):
    artist = models.CharField(max_length=250)
    albumTitle = models.CharField(max_length=500)
    genre = models.CharField(max_length=100)
    albumLogo = models.FileField()

    # m4 fahim dih lzmitha eh
    def get_absolute_url(self):
        return reverse('music:details', kwargs={'pk': self.pk})

    def __str__(self):
        return self.albumTitle + " - " + self.artist


class Song(models.Model):
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    fileType = models.CharField(max_length=10)
    songTitle = models.CharField(max_length=250)
    isFavourite = models.BooleanField(default=False)

    def __str__(self):
        return self.songTitle
