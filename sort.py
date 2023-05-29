#!/usr/bin/env python3

##################################
# Amber J. | https://electri.dev #
##################################

import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import colorgram
from PIL import Image
import requests
import os
import glob

def get_album_colors(album_cover):
    image = Image.open(album_cover)
    colors = colorgram.extract(image, 12)
    rgb_colors = [(color.rgb.r, color.rgb.g, color.rgb.b) for color in colors]
    return rgb_colors

def get_song_details(uri):
    client_id = 'YOUR_CLIENT_ID'
    client_secret = 'YOUR_CLIENT_SECRET'
    sp = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id=client_id, client_secret=client_secret))

    if 'playlist' in uri:
        results = sp.playlist_tracks(uri)
        tracks = results['items']
        album_covers = []
        for track in tracks:
            album_cover_url = track['track']['album']['images'][0]['url']
            album_cover = f"{track['track']['album']['name'].replace(' ', '_')}.jpg"
            response = requests.get(album_cover_url)
            with open(album_cover, 'wb') as file:
                file.write(response.content)
            album_covers.append(album_cover)
    else:
        print("Invalid link. Please provide a valid Spotify playlist link.")
        return ""

    table = "| Song | Artist | Album | Length |\n| --- | --- | --- | --- |\n"

    sorted_tracks = sorted(tracks, key=lambda track: get_album_colors(album_covers.pop(0)))

    for track in sorted_tracks:
        song_name = track['track']['name']
        artist_name = track['track']['artists'][0]['name']
        album_name = track['track']['album']['name']
        duration_ms = track['track']['duration_ms']
        duration_min_sec = divmod(duration_ms // 1000, 60)
        length = f"{duration_min_sec[0]:02}:{duration_min_sec[1]:02}"
        table += f"| {song_name} | {artist_name} | {album_name} | {length} |\n"

    return table

uri = input("Enter a Spotify playlist link: ")
print("This may take a moment...")
output_table = get_song_details(uri)
print(output_table)
[os.remove(file_path) for file_path in glob.glob('./*.jpg')]
