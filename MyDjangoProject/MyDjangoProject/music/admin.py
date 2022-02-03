from django.contrib import admin

from .models import Album, Song

admin.site.register(Album)   # to show Album table on admin page
admin.site.register(Song)    # to show song table on admin page

