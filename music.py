#username = '31lkuauxoun3n66lzigaavqcgcsy'
#clientID = '60413857ed3c424988feec42521d1779'
#clientSecret = 'c7675b2c43b14400a2d009ec22d2003a'
#redirect_uri = 'http://google.com/callback/'
# shows artist info for a URN or URL

import json
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from pprint import pprint
from time import sleep
  
username = '31lkuauxoun3n66lzigaavqcgcsy'
clientID = '60413857ed3c424988feec42521d1779'
clientSecret = 'c7675b2c43b14400a2d009ec22d2003a'
redirect_uri = 'http://google.com/callback/'
#oauth_object = spotipy.SpotifyOAuth(clientID, clientSecret, redirect_uri)
#token_dict = oauth_object.get_access_token()
#token = token_dict['access_token']
#spotifyObject = spotipy.Spotify(auth=token)



scope = "user-read-playback-state,user-modify-playback-state,user-library-read"
sp = spotipy.Spotify(client_credentials_manager=SpotifyOAuth(client_id=clientID,
                                               client_secret=clientSecret,
                                               redirect_uri=redirect_uri,scope=scope))

results = sp.current_user_saved_tracks()
# Shows playing devices
res = sp.devices()
pprint(res)

#results = sp.current_user_saved_tracks()
user_name = sp.current_user()
  
# To print the JSON response from 
# browser in a readable format.
# optional can be removed
print(json.dumps(user_name, sort_keys=True, indent=4))
  
def play_song(search_song):
    if search_song != '':
        results = sp.search(search_song, 1, 0, "track")
        #print(results)
        songs_dict = results['tracks']
        song_items = songs_dict['items']
        song = song_items[0]['external_urls']['spotify']
        uri = song_items[0]['uri']
        #print(uri)
        sp.start_playback(uris=[uri],device_id='81e20d9708caf9b51b5851201c5777e929ae7601')

        # Change volume
        sp.volume(100)
        #webbrowser.open(song)
        print('正在播放')
def pause_play():
    sp.pause_playback()
#pause_play()
