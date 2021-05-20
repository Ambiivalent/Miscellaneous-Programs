import spotipy, json, os, matplotlib.pyplot
from spotipy.oauth2 import SpotifyClientCredentials

def show_tracks(results):
    tracks = []
    for items in results["items"]:
        if items["track"] is None: continue
        tracks.append(items["track"]["artists"][0]["name"])
    return tracks

def MergeDict(a,b):
    temp = {**a, **b}
    return temp

# TOKEN DATA GOES HERE
with open('tokens.json') as tokenData:
    tokens = json.load(tokenData)
    id = tokens["id"]
    secret = tokens["secret"]

client_credentials = SpotifyClientCredentials(client_id=id, client_secret=secret)
sp = spotipy.Spotify(client_credentials_manager = client_credentials)

# -------------------------------------------------------------------------------------------
user = "officebagel" # INSERT USERNAME HERE
# -------------------------------------------------------------------------------------------

playlists = sp.user_playlists(user)
data = {}

for playlist in playlists["items"]:
    totalArtists = 0
    artists = {}
    currentPlaylist = sp.playlist(playlist["id"], fields="tracks,next")
    tracks = currentPlaylist["tracks"]
    trackList = show_tracks(tracks)

    while tracks["next"]:
        tracks = sp.next(tracks)
        tempTracklist = show_tracks(tracks)
        for items in tempTracklist:
            trackList.append(items)

    for artist in trackList:
        if artist in artists: artists[artist] += 1
        else: artists[artist] = 1
        totalArtists += 1

    if playlist['name'] in data:
        data[playlist['name']][0] = MergeDict(data[playlist['name']][0], artists)
        data[playlist['name']][1] += totalArtists
    else: data[playlist['name']] = (artists, totalArtists)

# -------------------------------------------------------------------------------------------
playlist = "<relax>" # PLAYLIST NAME HERE
# -------------------------------------------------------------------------------------------

totalArtists = data[playlist][1]
dictOfArtists = data[playlist][0]
label,numOfArtists = [],[]

for x,y in dictOfArtists.items():
    label.append(x)
    numOfArtists.append(y)

matplotlib.pyplot.pie(numOfArtists, labels=label, autopct="%1.1f%%")
matplotlib.pyplot.title(playlist)
matplotlib.pyplot.axis("equal")
matplotlib.pyplot.show()
    
