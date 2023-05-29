# playlist_sort
Sorts a Spotify playlist by color of album cover into a markdown table.

Dependencies can be installed with: ```pip3 install spotipy colorgram.py pillow```

Create a Spotify Developer account (https://developer.spotify.com), create a new application, put name/description as whatever, set redirect URI to https://localhost:8888/callback Then you can get a Client ID and Client Secret and put them on lines 22 and 23

## THIS WILL DELETE ALL .JPG FILES IN THE CURRENT DIRECTORY
You can comment out or remove the last line if this would be destructive to you, but I included it to clean up the album covers it downloads to accomplish this.

WIP: Fix the authentication stuff to actually directly modify the playlist - but for now, you get a table :)
