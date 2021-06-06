import urllib.request, urllib.parse
import json

def inputs():
    artist=input('Enter artist name:')
    name=input('Enter song name:')
    return name, artist

def find(name,artist):
    url='https://api.lyrics.ovh/v1/'
    artist=urllib.parse.quote_plus(artist)
    name=urllib.parse.quote_plus(name)
    #print(artist, name)
    url=url+artist+'/'+name
    response=urllib.request.urlopen(url)
    data=response.read().decode()
    js=json.loads(data)
    print('\nHere is the lyrics \n')
    print(js['lyrics'])


try:
    name, artist=inputs()
    find(name,artist)
    pass
except:
    try:
        print('Song not found\nPlease Enter the exact spelling of artist and song\n')
        name, artist=inputs()
        find(name,artist)
    except:
        print('\nSorry song not found')
        

print('\nRefresh the page to find lyrics of another song')
