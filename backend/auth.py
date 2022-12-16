import spotipy
import os
#CLIENT_ID = "a747d052efc94b4a9b8db1bfd0c31fa1"
CLIENT_ID = "de196a5035cb451499b1a2b29c58aac9"
CLIENT_SECRET= "50a107e67115470f87f801954665b81b"
REDIRECT_URI= "http://localhost:5000"
SCOPE= "playlist-modify-public" # this will definitely need to change
UN= "ribbsauce"

# Temporarilly here
os.environ["SPOTIPY_CLIENT_ID"]=CLIENT_ID
os.environ["SPOTIPY_CLIENT_SECRET"]=CLIENT_SECRET
os.environ["SPOTIPY_REDIRECT_URI"]=REDIRECT_URI

sp_oauth = spotipy.oauth2.SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope=SCOPE,
    username=UN,
)

# sp = spotipy.Spotify(auth_manager=sp_oauth)
# sp.user_create_playlist()
# sp.search(q=myQuery, type='track')
#   i believe sp api queries take the form of "artist:<artist> track:<track> genre:<genre> etc.." (of type string)
