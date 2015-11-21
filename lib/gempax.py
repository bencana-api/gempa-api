#!/usr/bin/python

# gempax is another gempa API for recent earthquake occurance in Indonesia
# it's a data scraper which uses http://earthquaketrack.com/p/indonesia/recent as its scraper target.
#

from urllib import urlopen
from bs4 import BeautifulSoup as bs


def fetchdata():
    url = 'http://earthquaketrack.com/p/indonesia/recent'
    data = urlopen(url).read()
    return data

def fetchdatasoup(data):
    clean = []
    soup = bs(data)
    data = [tag.text for tag in soup.find_all("div", {"class":"quiet"})]

    for items in data:
        clean.append(items)

    return clean

def getgempa():
    data = fetchdatasoup(fetchdata())
    return data

def getmagnitude(data):
    return data[3]

def magdata(data):
    scale = []
    for i in range(len(data)):
        d = getmagnitude(data[i].split().encode('ascii'))
        scale.append(d)
    return scale

def rmpnct(data):
    clean = []
    for items in data:
        if items != ',':
            clean.append(items)
    return ''.join(clean)

def location(data):
    return data[8].encode('ascii')

def getalllocations(data):
    loc = []
    for x in range(len(data)):
        d = rmpnct(location(data[x].split()))
        loc.append(d)
    return loc

def occurance(data):
    # usage: occurance(getalllocations(getgempa()))
    # frequency of earthquake occurance
    occ = {}
    ban = []
    for i in data:
        if i not in ban:
            occ[i] = data.count(i)
    return occ

if __name__ == '__main__':
    print 'running test...'
    import matplotlib.pyplot as plt
    oc = occurance(getalllocations(getgempa()))
    plt.bar(range(len(oc)), oc.values(), align='center')
    plt.xticks(range(len(oc)), oc.keys())
    plt.show()
