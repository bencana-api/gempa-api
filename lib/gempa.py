#!/usr/bin/python

__author__ = 'vickydasta'

'''
about gempa-api v1.0
gempa-api is an interface for data retreival of current earthquake information
(longitude, lotitude, location, magnitude, and potential of Tsunami)

github.com/bencana-api/gempa-api
'''

try:
    from bs4 import BeautifulSoup as bs
    from urllib2 import urlopen
except ImportError:
    raise ImportError('see requirements.txt!')

def fetchdata():
    url = 'http://www.bmkg.go.id/BMKG_Pusat/Kualitas_Udara/Informasi_Partikulat.bmkg'
    data = urlopen(url).read()
    return data

def get(data):
    s = bs(data)
    data = s.find("div",{"class":"panel-default row"})
    return data.text.split()

def datagempa():
    return get(fetchdata())

if __name__ == '__main__':
    print get()
