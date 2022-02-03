from django.shortcuts import render, get_object_or_404
from .models import Album, Song  # for database connection


def index(request):
    all_albums = Album.objects.all()    # for database connection
    context = {'all_albums':all_albums }
    return render(request, 'music/index.html', context)


def detail(request, album_id):
    # try cha jagi
    # album = Album.objects.get(pk=album_id)
    album = get_object_or_404(Album, pk=album_id)
    return render(request, 'music/detail.html', {'album':album })

def Favorite(request, album_id):
    album = get_object_or_404(Album, pk=album_id)
    try:
        selected_song = album.song_set.get(pk=request.POST['song'])
    except (keyError, Song.DoesNotExist):
        return render(request, 'music/detail.html', {
            'album': album,
            'error_message': "you did not select a valid song"
        })
    else:
        selected_song.is_favorite =True
        selected_song.save()
        return render(request, 'music/detail.html', {'album': album})

