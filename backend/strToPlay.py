# File for the *algorithm*
import spotipy
import auth

sp = spotipy.Spotify(auth_manager=auth.sp_oauth)

#myQuery = "surfer"
#results = sp.search(q="track: " + myQuery, type='track')
#items = results['tracks']['items']
#
#for i in range(len(items)):
#    print(items[i]['name'], " | ", items[i]['artists'][0]['name'])

def getSongs(spSession, tarWords):
    """
    Input:
        spSession: spotipy session
        tarWords: List[str] that is user input that we want to replicate with titles in a playlist
    Return:
        List/Tuple of Spotify Track URIs 
    """
    # Development Notes
    #   Base case is not explicit, but implied in the case of 'trackList = []' upon  

    if len(tarWords) == 0:
        return []

    trackList = []

    # 1. Tokenize
    #words = tarWords.lower()
    words = [x.lower() for x in tarWords]

    # 2. Look for matching titles, prioritizing short titles
    for i in range(len(words)):
        target = " ".join(words[:i+1])
        results = spSession.search(q="track: "+target, type="track")['tracks']
        print(f"target #{i}: {target}")

        while(results['next'] != None):
            items = results['items']
            for j in range(len(items)):
                track = items[j]
                print(f"track name: {track['name']}")
                if track['name'].lower() == target:
                    nextTracks = getSongs(spSession, tarWords[i+1:])

                    # 1. Check if the process can finish with the word being added
                    if nextTracks == None:
                        continue
                    
                    # 2. If so, add this track and it's subsequent results
                    trackList.append(track)
                    trackList += nextTracks
                    break
            if len(trackList) > 0:
                break
            results = spSession.next(results)['tracks']

        if len(trackList) > 0:
            break
            
    if len(trackList) == 0:
        return None
    return trackList

myString = "Sad boy hours my love"
myList = myString.split()


def printSongNames(myList):
    for x in myList:
        print(x['name'], " | ", x['artists'][0]['name'])


printSongNames(getSongs(sp, myList)) 
