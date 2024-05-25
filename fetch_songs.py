import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import random
import json
from datetime import datetime

# Replace these with your own client_id and client_secret
CLIENT_ID = '618b04c9abf54af1944a6253e1edea50'
CLIENT_SECRET = '2251f505e6014defa225bd0f5fdcbad7'

sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET))

def get_random_tracks():
    results = sp.search(q='year:2024', type='track', limit=50)
    tracks = results['tracks']['items']
    random.shuffle(tracks)
    return tracks[:5]

def save_tracks_to_file(tracks, filename='songs.json'):
    with open(filename, 'w') as f:
        json.dump(tracks, f)

def main():
    tracks = get_random_tracks()
    formatted_tracks = [{'title': track['name'], 'artist': track['artists'][0]['name'], 'url': track['external_urls']['spotify']} for track in tracks]
    save_tracks_to_file(formatted_tracks)

if __name__ == "__main__":
    main()
