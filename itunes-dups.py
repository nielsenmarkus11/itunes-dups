
#%% Importing Libraries
import os
import time
from pathlib import Path
from filecmp import cmp
  
#%% list of all documents
foldername = "C:/Users/niels/Music/iTunes/iTunes Media/Music"
DATA_DIR = Path(foldername)
artists = sorted(os.listdir(DATA_DIR))

for artist in artists:
    albums = sorted(os.listdir(Path(foldername+'/'+artist)))

    for album in albums:
        songs = sorted(os.listdir(Path(foldername+'/'+artist+'/'+album)))

        deleted_songs = []
        for song in songs:
            song_name = song
            song_size = Path(foldername+'/'+artist+'/'+album+'/'+song).stat().st_size
            other_songs = list(set(songs) - set([song_name]))

            for osong in other_songs:
                if osong not in deleted_songs:
                    dupl_name = osong
                    dupl_size = Path(foldername+'/'+artist+'/'+album+'/'+dupl_name).stat().st_size
                    song_name_tmp = os.path.splitext(song_name)[0]
                    dupl_name_tmp = os.path.splitext(dupl_name)[0]
                    if song_name_tmp + " 1" == dupl_name_tmp:
                        print("Duplicate file: " + dupl_name)
                        os.remove(Path(foldername+'/'+artist+'/'+album+'/'+dupl_name))
                        deleted_songs.append(dupl_name)

# %%
