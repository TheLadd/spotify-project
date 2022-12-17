# File for the *algorithm*
import spotipy
import auth

sp = spotipy.Spotify(auth_manager=auth.sp_oauth)

def getSongs(spSession, tarWords):
    """
    Input:
        spSession: spotipy session
        tarWords: List[str] that is user input that we want to replicate with titles in a playlist
    Return:
        List of Spotify Track URIs 
    """

    # Base case
    if len(tarWords) == 0:
        return []

    # 1. Pre-process
    words = [x.lower() for x in tarWords]

    # 2. Look for titles matching the first i words (prioritizing short titles)
    for i in range(len(words)):
        target = " ".join(words[:i+1])
        results = spSession.search(q="track: "+target, type="track")
        results = results['tracks']
        k = 0

        # Cycle through first 10 pages of search results
        while results['next'] != None and k < 10:
            items = results['items']

            # Look through a page of search results
            for j in range(len(items)):
                track = items[j]
                if track['name'].lower() == target:
                    nextTracks = getSongs(spSession, tarWords[i+1:])
                    if nextTracks != None:
                        return [track] + nextTracks
                    break

            k += 1
            results = spSession.next(results)['tracks']

    return None 

def printSongNames(myList):
    if myList == None:
        print("Couldn't find what you were looking for!")
        return
    for x in myList:
        print(x['name'], " | ", x['artists'][0]['name'])


#myString = "Sad boy hours my love"
myString = "I'm finding it hard to carry on"
myString = "Hey friend you suck"
myList = myString.split()
printSongNames(getSongs(sp, myList)) 
