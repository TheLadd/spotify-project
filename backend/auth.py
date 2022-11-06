import spotipy
# sp.user_create_playlist()
# sp.search(q=myQuery, type='track')
#   i believe sp api queries take the form of "artist:<artist> track:<track> genre:<genre> etc.." (of type string)

CLIENT_ID = "a747d052efc94b4a9b8db1bfd0c31fa1"
CLIENT_SECRET= "de5a3b6b6cd94d4f89444e187268a1bc"
REDIRECT_URI= "http://localhost:5000"
SCOPE= "playlist-modify-public" # this will definitely need to change
UN= "ribbsauce"

sp_oauth = spotipy.oauth2.SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope=SCOPE,
    username=UN,
)

#sp = spotipy.Spotify(auth_manager=sp_oauth)