# code journey
# gempax.py
# the script is yet written

```
In [28]: %paste
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
    for item in data:
        clean.append(item)
    return clean

def getgempa():
    data = fetchdatasoup(fetchdata())
    return data

## -- End pasted text --

In [29]: 

In [29]: ge
gempa-api/   get_ipython  getattr      getgempa     

In [29]: get
get_ipython  getattr      getgempa     

In [29]: data=getgempa()

In [30]: data
Out[30]: 
[u'\n\n\n\n        2015-11-21 09:06:12 UTC\n      \n\n\n6.1 magnitude, 67 km depth\n\nTual,\n      Indonesia\n',
 u'\n\n\n\n        2015-11-21 04:38:25 UTC\n      \n\n\n4.5 magnitude, 10 km depth\n\nTernate,\n      Indonesia\n',
 u'\n\n\n\n        2015-11-21 02:35:57 UTC\n      \n\n\n4.7 magnitude, 10 km depth\n\nTernate,\n      Indonesia\n',
 u'\n\n\n\n        2015-11-20 19:48:45 UTC\n      \n\n\n4.8 magnitude, 19 km depth\n\nLabuhan,\n      Indonesia\n',
 u'\n\n\n\n        2015-11-20 14:50:43 UTC\n      \n\n\n4.9 magnitude, 36 km depth\n\nTernate,\n      Indonesia\n',
 u'\n\n\n\n        2015-11-18 16:47:09 UTC\n      \n\n\n5.0 magnitude, 48 km depth\n\nBandar Lampung,\n        Lampung,\n      Indonesia\n',
 u'\n\n\n\n        2015-11-18 10:36:56 UTC\n      \n\n\n5.0 magnitude, 114 km depth\n\nBaturaja,\n      Indonesia\n',
 u'\n\n\n\n        2015-11-18 04:14:37 UTC\n      \n\n\n4.8 magnitude, 62 km depth\n\nBitung,\n        Sulawesi Utara,\n      Indonesia\n',
 u'\n\n\n\n        2015-11-17 12:51:03 UTC\n      \n\n\n4.8 magnitude, 10 km depth\n\nTernate,\n      Indonesia\n',
 u'\n\n\n\n        2015-11-16 03:11:48 UTC\n      \n\n\n4.6 magnitude, 10 km depth\n\nBima,\n        Nusa Tenggara Barat,\n      Indonesia\n',
 u'\n\n\n\n        2015-11-14 17:33:59 UTC\n      \n\n\n4.1 magnitude, 40 km depth\n\nSorong,\n      Indonesia\n',
 u'\n\n\n\n        2015-11-14 16:53:31 UTC\n      \n\n\n5.3 magnitude, 10 km depth\n\nSabang,\n        Aceh,\n      Indonesia\n',
 u'\n\n\n\n        2015-11-14 15:19:12 UTC\n      \n\n\n4.8 magnitude, 10 km depth\n\nTual,\n      Indonesia\n',
 u'\n\n\n\n        2015-11-12 22:38:00 UTC\n      \n\n\n4.7 magnitude, 59 km depth\n\nTernate,\n      Indonesia\n',
 u'\n\n\n\n        2015-11-12 17:50:37 UTC\n      \n\n\n4.7 magnitude, 48 km depth\n\nBandar Lampung,\n        Lampung,\n      Indonesia\n',
 u'\n\n\n\n        2015-11-12 02:34:44 UTC\n      \n\n\n4.3 magnitude, 78 km depth\n\nGondanglegi,\n        Jawa Timur,\n      Indonesia\n',
 u'\n\n\n\n        2015-11-11 22:17:59 UTC\n      \n\n\n5.2 magnitude, 100 km depth\n\nTernate,\n      Indonesia\n',
 u'\n\n\n\n        2015-11-11 11:45:23 UTC\n      \n\n\n5.6 magnitude, 77 km depth\n\nBambanglipuro,\n        Yogyakarta,\n      Indonesia\n',
 u'\n\n\n\n        2015-11-10 23:07:50 UTC\n      \n\n\n4.2 magnitude, 280 km depth\n\nBima,\n        Nusa Tenggara Barat,\n      Indonesia\n',
 u'\n\n\n\n        2015-11-10 18:49:53 UTC\n      \n\n\n4.5 magnitude, 97 km depth\n\nKupang,\n        Nusa Tenggara Timur,\n      Indonesia\n',
 u'\n\n\n\n        2015-11-10 08:58:43 UTC\n      \n\n\n4.7 magnitude, 141 km depth\n\nGorontalo,\n        Sulawesi Utara,\n      Indonesia\n',
 u'\n\n\n\n        2015-11-09 08:12:49 UTC\n      \n\n\n5.5 magnitude, 35 km depth\n\nSabang,\n        Aceh,\n      Indonesia\n',
 u'\n\n\n\n        2015-11-09 07:13:30 UTC\n      \n\n\n4.9 magnitude, 35 km depth\n\nSabang,\n        Aceh,\n      Indonesia\n',
 u'\n\n\n\n        2015-11-09 07:07:47 UTC\n      \n\n\n4.7 magnitude, 35 km depth\n\nSabang,\n        Aceh,\n      Indonesia\n',
 u'\n\n\n\n        2015-11-09 06:12:18 UTC\n      \n\n\n5.3 magnitude, 43 km depth\n\nSabang,\n        Aceh,\n      Indonesia\n',
 u'\n\n\n\n        2015-11-08 20:59:39 UTC\n      \n\n\n4.9 magnitude, 10 km depth\n\nSabang,\n        Aceh,\n      Indonesia\n',
 u'\n\n\n\n        2015-11-08 20:30:06 UTC\n      \n\n\n4.7 magnitude, 10 km depth\n\nSabang,\n        Aceh,\n      Indonesia\n',
 u'\n\n\n\n        2015-11-08 19:14:46 UTC\n      \n\n\n5.0 magnitude, 10 km depth\n\nSabang,\n        Aceh,\n      Indonesia\n',
 u'\n\n\n\n        2015-11-08 18:48:44 UTC\n      \n\n\n4.6 magnitude, 10 km depth\n\nSabang,\n        Aceh,\n      Indonesia\n',
 u'\n\n\n\n        2015-11-08 17:46:51 UTC\n      \n\n\n4.7 magnitude, 10 km depth\n\nSabang,\n        Aceh,\n      Indonesia\n']

In [31]: 

In [31]: data
Out[31]: 
[u'\n\n\n\n        2015-11-21 09:06:12 UTC\n      \n\n\n6.1 magnitude, 67 km depth\n\nTual,\n      Indonesia\n',
 u'\n\n\n\n        2015-11-21 04:38:25 UTC\n      \n\n\n4.5 magnitude, 10 km depth\n\nTernate,\n      Indonesia\n',
 u'\n\n\n\n        2015-11-21 02:35:57 UTC\n      \n\n\n4.7 magnitude, 10 km depth\n\nTernate,\n      Indonesia\n',
 u'\n\n\n\n        2015-11-20 19:48:45 UTC\n      \n\n\n4.8 magnitude, 19 km depth\n\nLabuhan,\n      Indonesia\n',
 u'\n\n\n\n        2015-11-20 14:50:43 UTC\n      \n\n\n4.9 magnitude, 36 km depth\n\nTernate,\n      Indonesia\n',
 u'\n\n\n\n        2015-11-18 16:47:09 UTC\n      \n\n\n5.0 magnitude, 48 km depth\n\nBandar Lampung,\n        Lampung,\n      Indonesia\n',
 u'\n\n\n\n        2015-11-18 10:36:56 UTC\n      \n\n\n5.0 magnitude, 114 km depth\n\nBaturaja,\n      Indonesia\n',
 u'\n\n\n\n        2015-11-18 04:14:37 UTC\n      \n\n\n4.8 magnitude, 62 km depth\n\nBitung,\n        Sulawesi Utara,\n      Indonesia\n',
 u'\n\n\n\n        2015-11-17 12:51:03 UTC\n      \n\n\n4.8 magnitude, 10 km depth\n\nTernate,\n      Indonesia\n',
 u'\n\n\n\n        2015-11-16 03:11:48 UTC\n      \n\n\n4.6 magnitude, 10 km depth\n\nBima,\n        Nusa Tenggara Barat,\n      Indonesia\n',
 u'\n\n\n\n        2015-11-14 17:33:59 UTC\n      \n\n\n4.1 magnitude, 40 km depth\n\nSorong,\n      Indonesia\n',
 u'\n\n\n\n        2015-11-14 16:53:31 UTC\n      \n\n\n5.3 magnitude, 10 km depth\n\nSabang,\n        Aceh,\n      Indonesia\n',
 u'\n\n\n\n        2015-11-14 15:19:12 UTC\n      \n\n\n4.8 magnitude, 10 km depth\n\nTual,\n      Indonesia\n',
 u'\n\n\n\n        2015-11-12 22:38:00 UTC\n      \n\n\n4.7 magnitude, 59 km depth\n\nTernate,\n      Indonesia\n',
 u'\n\n\n\n        2015-11-12 17:50:37 UTC\n      \n\n\n4.7 magnitude, 48 km depth\n\nBandar Lampung,\n        Lampung,\n      Indonesia\n',
 u'\n\n\n\n        2015-11-12 02:34:44 UTC\n      \n\n\n4.3 magnitude, 78 km depth\n\nGondanglegi,\n        Jawa Timur,\n      Indonesia\n',
 u'\n\n\n\n        2015-11-11 22:17:59 UTC\n      \n\n\n5.2 magnitude, 100 km depth\n\nTernate,\n      Indonesia\n',
 u'\n\n\n\n        2015-11-11 11:45:23 UTC\n      \n\n\n5.6 magnitude, 77 km depth\n\nBambanglipuro,\n        Yogyakarta,\n      Indonesia\n',
 u'\n\n\n\n        2015-11-10 23:07:50 UTC\n      \n\n\n4.2 magnitude, 280 km depth\n\nBima,\n        Nusa Tenggara Barat,\n      Indonesia\n',
 u'\n\n\n\n        2015-11-10 18:49:53 UTC\n      \n\n\n4.5 magnitude, 97 km depth\n\nKupang,\n        Nusa Tenggara Timur,\n      Indonesia\n',
 u'\n\n\n\n        2015-11-10 08:58:43 UTC\n      \n\n\n4.7 magnitude, 141 km depth\n\nGorontalo,\n        Sulawesi Utara,\n      Indonesia\n',
 u'\n\n\n\n        2015-11-09 08:12:49 UTC\n      \n\n\n5.5 magnitude, 35 km depth\n\nSabang,\n        Aceh,\n      Indonesia\n',
 u'\n\n\n\n        2015-11-09 07:13:30 UTC\n      \n\n\n4.9 magnitude, 35 km depth\n\nSabang,\n        Aceh,\n      Indonesia\n',
 u'\n\n\n\n        2015-11-09 07:07:47 UTC\n      \n\n\n4.7 magnitude, 35 km depth\n\nSabang,\n        Aceh,\n      Indonesia\n',
 u'\n\n\n\n        2015-11-09 06:12:18 UTC\n      \n\n\n5.3 magnitude, 43 km depth\n\nSabang,\n        Aceh,\n      Indonesia\n',
 u'\n\n\n\n        2015-11-08 20:59:39 UTC\n      \n\n\n4.9 magnitude, 10 km depth\n\nSabang,\n        Aceh,\n      Indonesia\n',
 u'\n\n\n\n        2015-11-08 20:30:06 UTC\n      \n\n\n4.7 magnitude, 10 km depth\n\nSabang,\n        Aceh,\n      Indonesia\n',
 u'\n\n\n\n        2015-11-08 19:14:46 UTC\n      \n\n\n5.0 magnitude, 10 km depth\n\nSabang,\n        Aceh,\n      Indonesia\n',
 u'\n\n\n\n        2015-11-08 18:48:44 UTC\n      \n\n\n4.6 magnitude, 10 km depth\n\nSabang,\n        Aceh,\n      Indonesia\n',
 u'\n\n\n\n        2015-11-08 17:46:51 UTC\n      \n\n\n4.7 magnitude, 10 km depth\n\nSabang,\n        Aceh,\n      Indonesia\n']

In [32]: def rm(x):
   ....:     for i in x:
   ....:         if i != '\n':
   ....:             
KeyboardInterrupt

In [32]: def rm(x):
    for i in x:
        if i != '\n':
KeyboardInterrupt

In [32]: def rm(x):
   ....:     c = []
   ....:     for i in x:
   ....:         if i != '
   ....:         
KeyboardInterrupt

In [32]: def rm(x):
   ....:     c = []
   ....:     for i in xL
   ....:     if
KeyboardInterrupt

In [32]: def 
KeyboardInterrupt

In [32]: data[0]
Out[32]: u'\n\n\n\n        2015-11-21 09:06:12 UTC\n      \n\n\n6.1 magnitude, 67 km depth\n\nTual,\n      Indonesia\n'

In [33]: data[0].split()
Out[33]: 
[u'2015-11-21',
 u'09:06:12',
 u'UTC',
 u'6.1',
 u'magnitude,',
 u'67',
 u'km',
 u'depth',
 u'Tual,',
 u'Indonesia']

In [34]: data[2].split()
Out[34]: 
[u'2015-11-21',
 u'02:35:57',
 u'UTC',
 u'4.7',
 u'magnitude,',
 u'10',
 u'km',
 u'depth',
 u'Ternate,',
 u'Indonesia']

In [35]: for x in data:
   ....:     print x.split()
   ....:     
[u'2015-11-21', u'09:06:12', u'UTC', u'6.1', u'magnitude,', u'67', u'km', u'depth', u'Tual,', u'Indonesia']
[u'2015-11-21', u'04:38:25', u'UTC', u'4.5', u'magnitude,', u'10', u'km', u'depth', u'Ternate,', u'Indonesia']
[u'2015-11-21', u'02:35:57', u'UTC', u'4.7', u'magnitude,', u'10', u'km', u'depth', u'Ternate,', u'Indonesia']
[u'2015-11-20', u'19:48:45', u'UTC', u'4.8', u'magnitude,', u'19', u'km', u'depth', u'Labuhan,', u'Indonesia']
[u'2015-11-20', u'14:50:43', u'UTC', u'4.9', u'magnitude,', u'36', u'km', u'depth', u'Ternate,', u'Indonesia']
[u'2015-11-18', u'16:47:09', u'UTC', u'5.0', u'magnitude,', u'48', u'km', u'depth', u'Bandar', u'Lampung,', u'Lampung,', u'Indonesia']
[u'2015-11-18', u'10:36:56', u'UTC', u'5.0', u'magnitude,', u'114', u'km', u'depth', u'Baturaja,', u'Indonesia']
[u'2015-11-18', u'04:14:37', u'UTC', u'4.8', u'magnitude,', u'62', u'km', u'depth', u'Bitung,', u'Sulawesi', u'Utara,', u'Indonesia']
[u'2015-11-17', u'12:51:03', u'UTC', u'4.8', u'magnitude,', u'10', u'km', u'depth', u'Ternate,', u'Indonesia']
[u'2015-11-16', u'03:11:48', u'UTC', u'4.6', u'magnitude,', u'10', u'km', u'depth', u'Bima,', u'Nusa', u'Tenggara', u'Barat,', u'Indonesia']
[u'2015-11-14', u'17:33:59', u'UTC', u'4.1', u'magnitude,', u'40', u'km', u'depth', u'Sorong,', u'Indonesia']
[u'2015-11-14', u'16:53:31', u'UTC', u'5.3', u'magnitude,', u'10', u'km', u'depth', u'Sabang,', u'Aceh,', u'Indonesia']
[u'2015-11-14', u'15:19:12', u'UTC', u'4.8', u'magnitude,', u'10', u'km', u'depth', u'Tual,', u'Indonesia']
[u'2015-11-12', u'22:38:00', u'UTC', u'4.7', u'magnitude,', u'59', u'km', u'depth', u'Ternate,', u'Indonesia']
[u'2015-11-12', u'17:50:37', u'UTC', u'4.7', u'magnitude,', u'48', u'km', u'depth', u'Bandar', u'Lampung,', u'Lampung,', u'Indonesia']
[u'2015-11-12', u'02:34:44', u'UTC', u'4.3', u'magnitude,', u'78', u'km', u'depth', u'Gondanglegi,', u'Jawa', u'Timur,', u'Indonesia']
[u'2015-11-11', u'22:17:59', u'UTC', u'5.2', u'magnitude,', u'100', u'km', u'depth', u'Ternate,', u'Indonesia']
[u'2015-11-11', u'11:45:23', u'UTC', u'5.6', u'magnitude,', u'77', u'km', u'depth', u'Bambanglipuro,', u'Yogyakarta,', u'Indonesia']
[u'2015-11-10', u'23:07:50', u'UTC', u'4.2', u'magnitude,', u'280', u'km', u'depth', u'Bima,', u'Nusa', u'Tenggara', u'Barat,', u'Indonesia']
[u'2015-11-10', u'18:49:53', u'UTC', u'4.5', u'magnitude,', u'97', u'km', u'depth', u'Kupang,', u'Nusa', u'Tenggara', u'Timur,', u'Indonesia']
[u'2015-11-10', u'08:58:43', u'UTC', u'4.7', u'magnitude,', u'141', u'km', u'depth', u'Gorontalo,', u'Sulawesi', u'Utara,', u'Indonesia']
[u'2015-11-09', u'08:12:49', u'UTC', u'5.5', u'magnitude,', u'35', u'km', u'depth', u'Sabang,', u'Aceh,', u'Indonesia']
[u'2015-11-09', u'07:13:30', u'UTC', u'4.9', u'magnitude,', u'35', u'km', u'depth', u'Sabang,', u'Aceh,', u'Indonesia']
[u'2015-11-09', u'07:07:47', u'UTC', u'4.7', u'magnitude,', u'35', u'km', u'depth', u'Sabang,', u'Aceh,', u'Indonesia']
[u'2015-11-09', u'06:12:18', u'UTC', u'5.3', u'magnitude,', u'43', u'km', u'depth', u'Sabang,', u'Aceh,', u'Indonesia']
[u'2015-11-08', u'20:59:39', u'UTC', u'4.9', u'magnitude,', u'10', u'km', u'depth', u'Sabang,', u'Aceh,', u'Indonesia']
[u'2015-11-08', u'20:30:06', u'UTC', u'4.7', u'magnitude,', u'10', u'km', u'depth', u'Sabang,', u'Aceh,', u'Indonesia']
[u'2015-11-08', u'19:14:46', u'UTC', u'5.0', u'magnitude,', u'10', u'km', u'depth', u'Sabang,', u'Aceh,', u'Indonesia']
[u'2015-11-08', u'18:48:44', u'UTC', u'4.6', u'magnitude,', u'10', u'km', u'depth', u'Sabang,', u'Aceh,', u'Indonesia']
[u'2015-11-08', u'17:46:51', u'UTC', u'4.7', u'magnitude,', u'10', u'km', u'depth', u'Sabang,', u'Aceh,', u'Indonesia']

In [36]: for x in data:
    print x.split()
KeyboardInterrupt

In [36]: def getdata(x):
   ....:     
, x[8], x[9] date, time, mag, depth, loc, country = x[0], x[1], x[3], x[5], x[7] 
   ....:     
   ....:     return (date, time, mag, depth, loc, country)
   ....:     
   ....:     
KeyboardInterrupt


In [36]: 

In [36]: def getdata(x):
, x[8], x[9] date, time, mag, depth, loc, country = x[0], x[1], x[3], x[5], x[7] 
   ....:     data = (date, mag, depth, loc, country)
   ....:     return data
   ....: 

In [37]: getdata(data[0])
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-37-6f476a53fdf1> in <module>()
----> 1 getdata(data[0])

<ipython-input-36-e07a70ba9862> in getdata(x)
      1 def getdata(x):
----> 2     date, time, mag, depth, loc, country = x[0], x[1], x[3], x[5], x[7], x[8], x[9]
      3     data = (date, mag, depth, loc, country)
      4     return data
      5 

ValueError: too many values to unpack

In [38]: getdata(data[0])
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-38-6f476a53fdf1> in <module>()
----> 1 getdata(data[0])

<ipython-input-36-e07a70ba9862> in getdata(x)
      1 def getdata(x):
----> 2     date, time, mag, depth, loc, country = x[0], x[1], x[3], x[5], x[7], x[8], x[9]
      3     data = (date, mag, depth, loc, country)
      4     return data
      5 

ValueError: too many values to unpack

In [39]: data[0]
Out[39]: u'\n\n\n\n        2015-11-21 09:06:12 UTC\n      \n\n\n6.1 magnitude, 67 km depth\n\nTual,\n      Indonesia\n'

In [40]: data[0].split()
Out[40]: 
[u'2015-11-21',
 u'09:06:12',
 u'UTC',
 u'6.1',
 u'magnitude,',
 u'67',
 u'km',
 u'depth',
 u'Tual,',
 u'Indonesia']

In [41]: def getmagnitude(x):
   ....:     return x[3]
   ....: 

In [42]: getmagnitude(data[1]
   ....: )
Out[42]: u'\n'

In [43]: getmagnitude(data[1]
)
KeyboardInterrupt

In [43]: getmagnitude(data[1]
.split())
Out[43]: u'4.5'

In [44]: 

In [44]: getmagnitude(data[1]
.split()).encode('ascii')
Out[44]: '4.5'

In [45]: int(getmagnitude(data[1]
.split()).encode('ascii'))
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-45-bc937b400cfb> in <module>()
      1 int(getmagnitude(data[1]
----> 2 .split()).encode('ascii'))

ValueError: invalid literal for int() with base 10: '4.5'

In [46]: float(getmagnitude(data[1]
.split()).encode('ascii'))
Out[46]: 4.5

In [47]: for u in data.split():
   ....:     
KeyboardInterrupt

In [47]: scale = []

In [48]: for u in data.split():
   ....:     scale.append(float(getmagnitude(u).encode('ascii'))
   ....:     
   ....:     )
   ....:     
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-48-9f8f6d5f8423> in <module>()
----> 1 for u in data.split():
      2     scale.append(float(getmagnitude(u).encode('ascii'))
      3 
      4     )
      5 

AttributeError: 'list' object has no attribute 'split'

In [49]: for u in data.split():
    scale.append(float(getmagnitude(u).encode('ascii'))
    
    )
KeyboardInterrupt

In [49]: data.split()
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-49-212a23571d6a> in <module>()
----> 1 data.split()

AttributeError: 'list' object has no attribute 'split'

In [50]: data
Out[50]: 
[u'\n\n\n\n        2015-11-21 09:06:12 UTC\n      \n\n\n6.1 magnitude, 67 km depth\n\nTual,\n      Indonesia\n',
 u'\n\n\n\n        2015-11-21 04:38:25 UTC\n      \n\n\n4.5 magnitude, 10 km depth\n\nTernate,\n      Indonesia\n',
 u'\n\n\n\n        2015-11-21 02:35:57 UTC\n      \n\n\n4.7 magnitude, 10 km depth\n\nTernate,\n      Indonesia\n',
 u'\n\n\n\n        2015-11-20 19:48:45 UTC\n      \n\n\n4.8 magnitude, 19 km depth\n\nLabuhan,\n      Indonesia\n',
 u'\n\n\n\n        2015-11-20 14:50:43 UTC\n      \n\n\n4.9 magnitude, 36 km depth\n\nTernate,\n      Indonesia\n',
 u'\n\n\n\n        2015-11-18 16:47:09 UTC\n      \n\n\n5.0 magnitude, 48 km depth\n\nBandar Lampung,\n        Lampung,\n      Indonesia\n',
 u'\n\n\n\n        2015-11-18 10:36:56 UTC\n      \n\n\n5.0 magnitude, 114 km depth\n\nBaturaja,\n      Indonesia\n',
 u'\n\n\n\n        2015-11-18 04:14:37 UTC\n      \n\n\n4.8 magnitude, 62 km depth\n\nBitung,\n        Sulawesi Utara,\n      Indonesia\n',
 u'\n\n\n\n        2015-11-17 12:51:03 UTC\n      \n\n\n4.8 magnitude, 10 km depth\n\nTernate,\n      Indonesia\n',
 u'\n\n\n\n        2015-11-16 03:11:48 UTC\n      \n\n\n4.6 magnitude, 10 km depth\n\nBima,\n        Nusa Tenggara Barat,\n      Indonesia\n',
 u'\n\n\n\n        2015-11-14 17:33:59 UTC\n      \n\n\n4.1 magnitude, 40 km depth\n\nSorong,\n      Indonesia\n',
 u'\n\n\n\n        2015-11-14 16:53:31 UTC\n      \n\n\n5.3 magnitude, 10 km depth\n\nSabang,\n        Aceh,\n      Indonesia\n',
 u'\n\n\n\n        2015-11-14 15:19:12 UTC\n      \n\n\n4.8 magnitude, 10 km depth\n\nTual,\n      Indonesia\n',
 u'\n\n\n\n        2015-11-12 22:38:00 UTC\n      \n\n\n4.7 magnitude, 59 km depth\n\nTernate,\n      Indonesia\n',
 u'\n\n\n\n        2015-11-12 17:50:37 UTC\n      \n\n\n4.7 magnitude, 48 km depth\n\nBandar Lampung,\n        Lampung,\n      Indonesia\n',
 u'\n\n\n\n        2015-11-12 02:34:44 UTC\n      \n\n\n4.3 magnitude, 78 km depth\n\nGondanglegi,\n        Jawa Timur,\n      Indonesia\n',
 u'\n\n\n\n        2015-11-11 22:17:59 UTC\n      \n\n\n5.2 magnitude, 100 km depth\n\nTernate,\n      Indonesia\n',
 u'\n\n\n\n        2015-11-11 11:45:23 UTC\n      \n\n\n5.6 magnitude, 77 km depth\n\nBambanglipuro,\n        Yogyakarta,\n      Indonesia\n',
 u'\n\n\n\n        2015-11-10 23:07:50 UTC\n      \n\n\n4.2 magnitude, 280 km depth\n\nBima,\n        Nusa Tenggara Barat,\n      Indonesia\n',
 u'\n\n\n\n        2015-11-10 18:49:53 UTC\n      \n\n\n4.5 magnitude, 97 km depth\n\nKupang,\n        Nusa Tenggara Timur,\n      Indonesia\n',
 u'\n\n\n\n        2015-11-10 08:58:43 UTC\n      \n\n\n4.7 magnitude, 141 km depth\n\nGorontalo,\n        Sulawesi Utara,\n      Indonesia\n',
 u'\n\n\n\n        2015-11-09 08:12:49 UTC\n      \n\n\n5.5 magnitude, 35 km depth\n\nSabang,\n        Aceh,\n      Indonesia\n',
 u'\n\n\n\n        2015-11-09 07:13:30 UTC\n      \n\n\n4.9 magnitude, 35 km depth\n\nSabang,\n        Aceh,\n      Indonesia\n',
 u'\n\n\n\n        2015-11-09 07:07:47 UTC\n      \n\n\n4.7 magnitude, 35 km depth\n\nSabang,\n        Aceh,\n      Indonesia\n',
 u'\n\n\n\n        2015-11-09 06:12:18 UTC\n      \n\n\n5.3 magnitude, 43 km depth\n\nSabang,\n        Aceh,\n      Indonesia\n',
 u'\n\n\n\n        2015-11-08 20:59:39 UTC\n      \n\n\n4.9 magnitude, 10 km depth\n\nSabang,\n        Aceh,\n      Indonesia\n',
 u'\n\n\n\n        2015-11-08 20:30:06 UTC\n      \n\n\n4.7 magnitude, 10 km depth\n\nSabang,\n        Aceh,\n      Indonesia\n',
 u'\n\n\n\n        2015-11-08 19:14:46 UTC\n      \n\n\n5.0 magnitude, 10 km depth\n\nSabang,\n        Aceh,\n      Indonesia\n',
 u'\n\n\n\n        2015-11-08 18:48:44 UTC\n      \n\n\n4.6 magnitude, 10 km depth\n\nSabang,\n        Aceh,\n      Indonesia\n',
 u'\n\n\n\n        2015-11-08 17:46:51 UTC\n      \n\n\n4.7 magnitude, 10 km depth\n\nSabang,\n        Aceh,\n      Indonesia\n']

In [51]: data.split('')
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-51-09d8f68b7e85> in <module>()
----> 1 data.split('')

AttributeError: 'list' object has no attribute 'split'

In [52]: for u in data:
    scale.append(float(getmagnitude(u).encode('ascii'))
    
    )
KeyboardInterrupt

In [52]: for i in data:
   ....:     for u in i:
   ....:         mag = float(getmagnitude(u).encode('ascii')))
   ....:         scale.append(mag)
   ....:         
  File "<ipython-input-52-c232535544f1>", line 3
    mag = float(getmagnitude(u).encode('ascii')))
                                                ^
SyntaxError: invalid syntax


In [53]: for i in data:
    for u in i:
        mag = float(getmagnitude(u).encode('ascii')) 
        scale.append(mag)
   ....:         
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
<ipython-input-53-e5d176201968> in <module>()
      1 for i in data:
      2     for u in i:
----> 3         mag = float(getmagnitude(u).encode('ascii'))
      4         scale.append(mag)
      5 

<ipython-input-41-2b866f21addb> in getmagnitude(x)
      1 def getmagnitude(x):
----> 2     return x[3]
      3 

IndexError: string index out of range

In [54]: for i in data:
    for u in i.split():
        mag = float(getmagnitude(u).encode('ascii'))
        scale.append(mag)
   ....:         
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
<ipython-input-54-9bf26b52388a> in <module>()
      1 for i in data:
      2     for u in i.split():
----> 3         mag = float(getmagnitude(u).encode('ascii'))
      4         scale.append(mag)
      5 

<ipython-input-41-2b866f21addb> in getmagnitude(x)
      1 def getmagnitude(x):
----> 2     return x[3]
      3 

IndexError: string index out of range

In [55]: for x in data.split():
KeyboardInterrupt

In [55]: 

In [55]: raw = []

In [56]: for x in data.split():
   ....:     raw.append(x)
   ....:     
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-56-100c2782b44d> in <module>()
----> 1 for x in data.split():
      2     raw.append(x)
      3 

AttributeError: 'list' object has no attribute 'split'

In [57]: for x.split() in data:
    raw.append(x)
   ....:     
  File "<ipython-input-57-f6a93740ae90>", line 1
    for x.split() in data:
SyntaxError: can't assign to function call


In [58]: for x in data:
   ....:     for i in x.split():
   ....:         raw.append(i)
   ....:         

In [59]: raw
Out[59]: 
[u'2015-11-21',
 u'09:06:12',
 u'UTC',
 u'6.1',
 u'magnitude,',
 u'67',
 u'km',
 u'depth',
 u'Tual,',
 u'Indonesia',
 u'2015-11-21',
 u'04:38:25',
 u'UTC',
 u'4.5',
 u'magnitude,',
 u'10',
 u'km',
 u'depth',
 u'Ternate,',
 u'Indonesia',
 u'2015-11-21',
 u'02:35:57',
 u'UTC',
 u'4.7',
 u'magnitude,',
 u'10',
 u'km',
 u'depth',
 u'Ternate,',
 u'Indonesia',
 u'2015-11-20',
 u'19:48:45',
 u'UTC',
 u'4.8',
 u'magnitude,',
 u'19',
 u'km',
 u'depth',
 u'Labuhan,',
 u'Indonesia',
 u'2015-11-20',
 u'14:50:43',
 u'UTC',
 u'4.9',
 u'magnitude,',
 u'36',
 u'km',
 u'depth',
 u'Ternate,',
 u'Indonesia',
 u'2015-11-18',
 u'16:47:09',
 u'UTC',
 u'5.0',
 u'magnitude,',
 u'48',
 u'km',
 u'depth',
 u'Bandar',
 u'Lampung,',
 u'Lampung,',
 u'Indonesia',
 u'2015-11-18',
 u'10:36:56',
 u'UTC',
 u'5.0',
 u'magnitude,',
 u'114',
 u'km',
 u'depth',
 u'Baturaja,',
 u'Indonesia',
 u'2015-11-18',
 u'04:14:37',
 u'UTC',
 u'4.8',
 u'magnitude,',
 u'62',
 u'km',
 u'depth',
 u'Bitung,',
 u'Sulawesi',
 u'Utara,',
 u'Indonesia',
 u'2015-11-17',
 u'12:51:03',
 u'UTC',
 u'4.8',
 u'magnitude,',
 u'10',
 u'km',
 u'depth',
 u'Ternate,',
 u'Indonesia',
 u'2015-11-16',
 u'03:11:48',
 u'UTC',
 u'4.6',
 u'magnitude,',
 u'10',
 u'km',
 u'depth',
 u'Bima,',
 u'Nusa',
 u'Tenggara',
 u'Barat,',
 u'Indonesia',
 u'2015-11-14',
 u'17:33:59',
 u'UTC',
 u'4.1',
 u'magnitude,',
 u'40',
 u'km',
 u'depth',
 u'Sorong,',
 u'Indonesia',
 u'2015-11-14',
 u'16:53:31',
 u'UTC',
 u'5.3',
 u'magnitude,',
 u'10',
 u'km',
 u'depth',
 u'Sabang,',
 u'Aceh,',
 u'Indonesia',
 u'2015-11-14',
 u'15:19:12',
 u'UTC',
 u'4.8',
 u'magnitude,',
 u'10',
 u'km',
 u'depth',
 u'Tual,',
 u'Indonesia',
 u'2015-11-12',
 u'22:38:00',
 u'UTC',
 u'4.7',
 u'magnitude,',
 u'59',
 u'km',
 u'depth',
 u'Ternate,',
 u'Indonesia',
 u'2015-11-12',
 u'17:50:37',
 u'UTC',
 u'4.7',
 u'magnitude,',
 u'48',
 u'km',
 u'depth',
 u'Bandar',
 u'Lampung,',
 u'Lampung,',
 u'Indonesia',
 u'2015-11-12',
 u'02:34:44',
 u'UTC',
 u'4.3',
 u'magnitude,',
 u'78',
 u'km',
 u'depth',
 u'Gondanglegi,',
 u'Jawa',
 u'Timur,',
 u'Indonesia',
 u'2015-11-11',
 u'22:17:59',
 u'UTC',
 u'5.2',
 u'magnitude,',
 u'100',
 u'km',
 u'depth',
 u'Ternate,',
 u'Indonesia',
 u'2015-11-11',
 u'11:45:23',
 u'UTC',
 u'5.6',
 u'magnitude,',
 u'77',
 u'km',
 u'depth',
 u'Bambanglipuro,',
 u'Yogyakarta,',
 u'Indonesia',
 u'2015-11-10',
 u'23:07:50',
 u'UTC',
 u'4.2',
 u'magnitude,',
 u'280',
 u'km',
 u'depth',
 u'Bima,',
 u'Nusa',
 u'Tenggara',
 u'Barat,',
 u'Indonesia',
 u'2015-11-10',
 u'18:49:53',
 u'UTC',
 u'4.5',
 u'magnitude,',
 u'97',
 u'km',
 u'depth',
 u'Kupang,',
 u'Nusa',
 u'Tenggara',
 u'Timur,',
 u'Indonesia',
 u'2015-11-10',
 u'08:58:43',
 u'UTC',
 u'4.7',
 u'magnitude,',
 u'141',
 u'km',
 u'depth',
 u'Gorontalo,',
 u'Sulawesi',
 u'Utara,',
 u'Indonesia',
 u'2015-11-09',
 u'08:12:49',
 u'UTC',
 u'5.5',
 u'magnitude,',
 u'35',
 u'km',
 u'depth',
 u'Sabang,',
 u'Aceh,',
 u'Indonesia',
 u'2015-11-09',
 u'07:13:30',
 u'UTC',
 u'4.9',
 u'magnitude,',
 u'35',
 u'km',
 u'depth',
 u'Sabang,',
 u'Aceh,',
 u'Indonesia',
 u'2015-11-09',
 u'07:07:47',
 u'UTC',
 u'4.7',
 u'magnitude,',
 u'35',
 u'km',
 u'depth',
 u'Sabang,',
 u'Aceh,',
 u'Indonesia',
 u'2015-11-09',
 u'06:12:18',
 u'UTC',
 u'5.3',
 u'magnitude,',
 u'43',
 u'km',
 u'depth',
 u'Sabang,',
 u'Aceh,',
 u'Indonesia',
 u'2015-11-08',
 u'20:59:39',
 u'UTC',
 u'4.9',
 u'magnitude,',
 u'10',
 u'km',
 u'depth',
 u'Sabang,',
 u'Aceh,',
 u'Indonesia',
 u'2015-11-08',
 u'20:30:06',
 u'UTC',
 u'4.7',
 u'magnitude,',
 u'10',
 u'km',
 u'depth',
 u'Sabang,',
 u'Aceh,',
 u'Indonesia',
 u'2015-11-08',
 u'19:14:46',
 u'UTC',
 u'5.0',
 u'magnitude,',
 u'10',
 u'km',
 u'depth',
 u'Sabang,',
 u'Aceh,',
 u'Indonesia',
 u'2015-11-08',
 u'18:48:44',
 u'UTC',
 u'4.6',
 u'magnitude,',
 u'10',
 u'km',
 u'depth',
 u'Sabang,',
 u'Aceh,',
 u'Indonesia',
 u'2015-11-08',
 u'17:46:51',
 u'UTC',
 u'4.7',
 u'magnitude,',
 u'10',
 u'km',
 u'depth',
 u'Sabang,',
 u'Aceh,',
 u'Indonesia']

In [60]: for x in data:
    for i in x.split():
        raw.append(i)
KeyboardInterrupt

In [60]: x 
Out[60]: u'\n\n\n\n        2015-11-08 17:46:51 UTC\n      \n\n\n4.7 magnitude, 10 km depth\n\nSabang,\n        Aceh,\n      Indonesia\n'

In [61]: x.split()
Out[61]: 
[u'2015-11-08',
 u'17:46:51',
 u'UTC',
 u'4.7',
 u'magnitude,',
 u'10',
 u'km',
 u'depth',
 u'Sabang,',
 u'Aceh,',
 u'Indonesia']

In [62]: getmagnitude(x.split())
Out[62]: u'4.7'

In [63]: for i in data:
   ....:     for u in data.split():
   ....:         d = getmagnitude(u)
   ....:         scale.append(d)
   ....:         
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-63-bc005bbd9594> in <module>()
      1 for i in data:
----> 2     for u in data.split():
      3         d = getmagnitude(u)
      4         scale.append(d)
      5 

AttributeError: 'list' object has no attribute 'split'

In [64]: for i in data:
    for u in i.split():
        d = getmagnitude(u)
        scale.append(d)
   ....:         
---------------------------------------------------------------------------
IndexError                                Traceback (most recent call last)
<ipython-input-64-b6da93dc173f> in <module>()
      1 for i in data:
      2     for u in i.split():
----> 3         d = getmagnitude(u)
      4         scale.append(d)
      5 

<ipython-input-41-2b866f21addb> in getmagnitude(x)
      1 def getmagnitude(x):
----> 2     return x[3]
      3 

IndexError: string index out of range

In [65]: for i in data:
    for u in i.split():
        print u
   ....:         
2015-11-21
09:06:12
UTC
6.1
magnitude,
67
km
depth
Tual,
Indonesia
2015-11-21
04:38:25
UTC
4.5
magnitude,
10
km
depth
Ternate,
Indonesia
2015-11-21
02:35:57
UTC
4.7
magnitude,
10
km
depth
Ternate,
Indonesia
2015-11-20
19:48:45
UTC
4.8
magnitude,
19
km
depth
Labuhan,
Indonesia
2015-11-20
14:50:43
UTC
4.9
magnitude,
36
km
depth
Ternate,
Indonesia
2015-11-18
16:47:09
UTC
5.0
magnitude,
48
km
depth
Bandar
Lampung,
Lampung,
Indonesia
2015-11-18
10:36:56
UTC
5.0
magnitude,
114
km
depth
Baturaja,
Indonesia
2015-11-18
04:14:37
UTC
4.8
magnitude,
62
km
depth
Bitung,
Sulawesi
Utara,
Indonesia
2015-11-17
12:51:03
UTC
4.8
magnitude,
10
km
depth
Ternate,
Indonesia
2015-11-16
03:11:48
UTC
4.6
magnitude,
10
km
depth
Bima,
Nusa
Tenggara
Barat,
Indonesia
2015-11-14
17:33:59
UTC
4.1
magnitude,
40
km
depth
Sorong,
Indonesia
2015-11-14
16:53:31
UTC
5.3
magnitude,
10
km
depth
Sabang,
Aceh,
Indonesia
2015-11-14
15:19:12
UTC
4.8
magnitude,
10
km
depth
Tual,
Indonesia
2015-11-12
22:38:00
UTC
4.7
magnitude,
59
km
depth
Ternate,
Indonesia
2015-11-12
17:50:37
UTC
4.7
magnitude,
48
km
depth
Bandar
Lampung,
Lampung,
Indonesia
2015-11-12
02:34:44
UTC
4.3
magnitude,
78
km
depth
Gondanglegi,
Jawa
Timur,
Indonesia
2015-11-11
22:17:59
UTC
5.2
magnitude,
100
km
depth
Ternate,
Indonesia
2015-11-11
11:45:23
UTC
5.6
magnitude,
77
km
depth
Bambanglipuro,
Yogyakarta,
Indonesia
2015-11-10
23:07:50
UTC
4.2
magnitude,
280
km
depth
Bima,
Nusa
Tenggara
Barat,
Indonesia
2015-11-10
18:49:53
UTC
4.5
magnitude,
97
km
depth
Kupang,
Nusa
Tenggara
Timur,
Indonesia
2015-11-10
08:58:43
UTC
4.7
magnitude,
141
km
depth
Gorontalo,
Sulawesi
Utara,
Indonesia
2015-11-09
08:12:49
UTC
5.5
magnitude,
35
km
depth
Sabang,
Aceh,
Indonesia
2015-11-09
07:13:30
UTC
4.9
magnitude,
35
km
depth
Sabang,
Aceh,
Indonesia
2015-11-09
07:07:47
UTC
4.7
magnitude,
35
km
depth
Sabang,
Aceh,
Indonesia
2015-11-09
06:12:18
UTC
5.3
magnitude,
43
km
depth
Sabang,
Aceh,
Indonesia
2015-11-08
20:59:39
UTC
4.9
magnitude,
10
km
depth
Sabang,
Aceh,
Indonesia
2015-11-08
20:30:06
UTC
4.7
magnitude,
10
km
depth
Sabang,
Aceh,
Indonesia
2015-11-08
19:14:46
UTC
5.0
magnitude,
10
km
depth
Sabang,
Aceh,
Indonesia
2015-11-08
18:48:44
UTC
4.6
magnitude,
10
km
depth
Sabang,
Aceh,
Indonesia
2015-11-08
17:46:51
UTC
4.7
magnitude,
10
km
depth
Sabang,
Aceh,
Indonesia

In [66]: for i in data:
    for u in i.split():
        print u
KeyboardInterrupt

In [66]: for i in range(len(data)):
   ....:     d = getmagnitude(data[i].split())
   ....:     scale.append(d)
   ....:     

In [67]: scale
Out[67]: 
[5.0,
 0.0,
 u'5',
 u'0',
 u'6.1',
 u'4.5',
 u'4.7',
 u'4.8',
 u'4.9',
 u'5.0',
 u'5.0',
 u'4.8',
 u'4.8',
 u'4.6',
 u'4.1',
 u'5.3',
 u'4.8',
 u'4.7',
 u'4.7',
 u'4.3',
 u'5.2',
 u'5.6',
 u'4.2',
 u'4.5',
 u'4.7',
 u'5.5',
 u'4.9',
 u'4.7',
 u'5.3',
 u'4.9',
 u'4.7',
 u'5.0',
 u'4.6',
 u'4.7']

In [68]: for i in range(len(data)):
    d = getmagnitude(data[i].split())
    scale.append(d)
KeyboardInterrupt

In [68]: for i in range(len(data)):
   ....:     d = float(getmagnitude(data[i].split()))
   ....:     
KeyboardInterrupt

In [68]: scale
Out[68]: 
[5.0,
 0.0,
 u'5',
 u'0',
 u'6.1',
 u'4.5',
 u'4.7',
 u'4.8',
 u'4.9',
 u'5.0',
 u'5.0',
 u'4.8',
 u'4.8',
 u'4.6',
 u'4.1',
 u'5.3',
 u'4.8',
 u'4.7',
 u'4.7',
 u'4.3',
 u'5.2',
 u'5.6',
 u'4.2',
 u'4.5',
 u'4.7',
 u'5.5',
 u'4.9',
 u'4.7',
 u'5.3',
 u'4.9',
 u'4.7',
 u'5.0',
 u'4.6',
 u'4.7']

In [69]: clear


In [70]: scale = []

In [71]: for x in range(len(data)):
   ....:     d = float(getmagnitude(x.split()).encode('ascii')))
   ....:     )
   ....:     
  File "<ipython-input-71-9a0f17fc0ebc>", line 2
    d = float(getmagnitude(x.split()).encode('ascii')))
                                                      ^
SyntaxError: invalid syntax


In [72]: for x in range(len(data)):
    d = float(getmagnitude(x.split()).encode('ascii')))
    
  File "<ipython-input-72-6adfb2f6d351>", line 2
    d = float(getmagnitude(x.split()).encode('ascii')))
                                                      ^
SyntaxError: invalid syntax


In [73]: 

In [73]: for x in range(len(data)):
    d = float(getmagnitude(x.split()).encode('ascii'))
   ....:     
---------------------------------------------------------------------------
AttributeError                            Traceback (most recent call last)
<ipython-input-73-b2c170eb883e> in <module>()
      1 for x in range(len(data)):
----> 2     d = float(getmagnitude(x.split()).encode('ascii'))
      3 

AttributeError: 'int' object has no attribute 'split'

In [74]: for x in range(len(data)):
    d = float(getmagnitude(data[x].split()).encode('ascii'))
   ....:     

In [75]: d
Out[75]: 4.7

In [76]: for x in range(len(data)):
    d = float(getmagnitude(data[x].split()).encode('ascii'))
   ....:     scale.append(d)
   ....:     

In [77]: scake
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-77-fb46de60f6b5> in <module>()
----> 1 scake

NameError: name 'scake' is not defined

In [78]: scale
Out[78]: 
[6.1,
 4.5,
 4.7,
 4.8,
 4.9,
 5.0,
 5.0,
 4.8,
 4.8,
 4.6,
 4.1,
 5.3,
 4.8,
 4.7,
 4.7,
 4.3,
 5.2,
 5.6,
 4.2,
 4.5,
 4.7,
 5.5,
 4.9,
 4.7,
 5.3,
 4.9,
 4.7,
 5.0,
 4.6,
 4.7]

In [79]: from matplotlib.pyplot as plt 
KeyboardInterrupt

In [79]: int(getmagnitude(data[1]
.split()).encode('ascii'))
KeyboardInterrupt

In [79]: import matplotlib.pyplot as plt

In [80]: plt.plot(scale)
Out[80]: [<matplotlib.lines.Line2D at 0x7f43b0b3a050>]

In [81]: plt.show()

In [82]:
    
In [92]: data[0].split().index(u'Tual,')
Out[92]: 8

In [93]: def rmpnct(x):
   ....:     if x != ',':
   ....:         

KeyboardInterrupt

In [93]: def rmpnct(x):
   ....:     d = []
   ....:     for i in x:
   ....:         if i != ',':
   ....:             d.append(i)
   ....:     return d
   ....: 

In [94]: def rmpnct(x):
    d = []
    for i in x:
        if i != ',':
            d.append(i)
    return ''.join(d)
   ....: 

In [95]: getloc(x):
   ....:     return x[8].encode('ascii')
  File "<ipython-input-95-85f95e371510>", line 1
    getloc(x):
             ^
SyntaxError: invalid syntax


In [96]: 

In [96]: def getloc(x):
    return x[8].encode('ascii')
   ....: 

In [97]: for i in range(len(data)):
   ....:     

KeyboardInterrupt

In [97]: loc
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-97-35e8fdf1750c> in <module>()
----> 1 loc

NameError: name 'loc' is not defined

In [98]: loc = []

In [99]: clear


In [100]: for x in range(len(data)):
   .....:     d = getloc(data[x].split())
   .....:     loc.append(d)
   .....:     

In [101]: loc
Out[101]: 
['Tual,',
 'Ternate,',
 'Ternate,',
 'Labuhan,',
 'Ternate,',
 'Bandar',
 'Baturaja,',
 'Bitung,',
 'Ternate,',
 'Bima,',
 'Sorong,',
 'Sabang,',
 'Tual,',
 'Ternate,',
 'Bandar',
 'Gondanglegi,',
 'Ternate,',
 'Bambanglipuro,',
 'Bima,',
 'Kupang,',
 'Gorontalo,',
 'Sabang,',
 'Sabang,',
 'Sabang,',
 'Sabang,',
 'Sabang,',
 'Sabang,',
 'Sabang,',
 'Sabang,',
 'Sabang,']

In [102]: loc.count('sabang')
Out[102]: 0

In [103]: loc.count('Sabang')
Out[103]: 0

In [104]: l = bs(i)

KeyboardInterrupt

In [104]: loc = []

In [105]: for x in range(len(data)):
    d = rmpnct(getloc(data[x].split()))
    loc.append(d)
   .....:     

In [106]: loc
Out[106]: 
['Tual',
 'Ternate',
 'Ternate',
 'Labuhan',
 'Ternate',
 'Bandar',
 'Baturaja',
 'Bitung',
 'Ternate',
 'Bima',
 'Sorong',
 'Sabang',
 'Tual',
 'Ternate',
 'Bandar',
 'Gondanglegi',
 'Ternate',
 'Bambanglipuro',
 'Bima',
 'Kupang',
 'Gorontalo',
 'Sabang',
 'Sabang',
 'Sabang',
 'Sabang',
 'Sabang',
 'Sabang',
 'Sabang',
 'Sabang',
 'Sabang']

In [107]: loc.count('Sabang')
Out[107]: 10

In [108]: occurance = []

In [109]: for i in loc:
   .....:     occurance.append(loc.count(i))
   .....:     

In [110]: oc
occurance  oct        

In [110]: occurance
Out[110]: 
[2,
 6,
 6,
 1,
 6,
 2,
 1,
 1,
 6,
 2,
 1,
 10,
 2,
 6,
 2,
 1,
 6,
 1,
 2,
 1,
 1,
 10,
 10,
 10,
 10,
 10,
 10,
 10,
 10,
 10]

In [111]: 

In [111]: occurance = []

In [112]: loc
Out[112]: 
['Tual',
 'Ternate',
 'Ternate',
 'Labuhan',
 'Ternate',
 'Bandar',
 'Baturaja',
 'Bitung',
 'Ternate',
 'Bima',
 'Sorong',
 'Sabang',
 'Tual',
 'Ternate',
 'Bandar',
 'Gondanglegi',
 'Ternate',
 'Bambanglipuro',
 'Bima',
 'Kupang',
 'Gorontalo',
 'Sabang',
 'Sabang',
 'Sabang',
 'Sabang',
 'Sabang',
 'Sabang',
 'Sabang',
 'Sabang',
 'Sabang']

In [113]: ban = []

In [114]: for i in loc:
   .....:     if i not in ban:
   .....:         occurance.append(loc.count(i))
   .....:         ban.append(i)
   .....:         

In [115]: occurance
Out[115]: [2, 6, 1, 2, 1, 1, 2, 1, 10, 1, 1, 1, 1]

In [116]: occurance = []

KeyboardInterrupt

In [116]: for i in loc:
    if i not in ban:
                                      
        ban.append(i)

KeyboardInterrupt

In [116]: oc = {}

In [117]: oc['a'] = {1)
  File "<ipython-input-117-5e95d49264ba>", line 1
    oc['a'] = {1)
                ^
SyntaxError: invalid syntax


In [118]: oc['a']
---------------------------------------------------------------------------
KeyError                                  Traceback (most recent call last)
<ipython-input-118-bfa04c271f0c> in <module>()
----> 1 oc['a']

KeyError: 'a'

In [119]: oc['a'] = [1]

In [120]: oc
Out[120]: {'a': [1]}

In [121]: oc['a'] = 1

In [122]: oc
Out[122]: {'a': 1}

In [123]: for i in loc:
    if i not in ban:
        occurance.append(loc.count(i))
        ban.append(i)

KeyboardInterrupt

In [123]: ban = []

In [124]: loc
Out[124]: 
['Tual',
 'Ternate',
 'Ternate',
 'Labuhan',
 'Ternate',
 'Bandar',
 'Baturaja',
 'Bitung',
 'Ternate',
 'Bima',
 'Sorong',
 'Sabang',
 'Tual',
 'Ternate',
 'Bandar',
 'Gondanglegi',
 'Ternate',
 'Bambanglipuro',
 'Bima',
 'Kupang',
 'Gorontalo',
 'Sabang',
 'Sabang',
 'Sabang',
 'Sabang',
 'Sabang',
 'Sabang',
 'Sabang',
 'Sabang',
 'Sabang']

In [125]: for i in loc:
   .....:     if i not in ban:
   .....:         

KeyboardInterrupt

In [125]: oc
Out[125]: {'a': 1}

In [126]: oc = {}

In [127]: for i in loc:
   .....:     if i not in ban:
   .....:         oc[i] = loc.count(i)
   .....:         

In [128]: oc
Out[128]: 
{'Bambanglipuro': 1,
 'Bandar': 2,
 'Baturaja': 1,
 'Bima': 2,
 'Bitung': 1,
 'Gondanglegi': 1,
 'Gorontalo': 1,
 'Kupang': 1,
 'Labuhan': 1,
 'Sabang': 10,
 'Sorong': 1,
 'Ternate': 6,
 'Tual': 2}

In [129]: 

In [135]: oc
Out[135]: 
{'Bambanglipuro': 1,
 'Bandar': 2,
 'Baturaja': 1,
 'Bima': 2,
 'Bitung': 1,
 'Gondanglegi': 1,
 'Gorontalo': 1,
 'Kupang': 1,
 'Labuhan': 1,
 'Sabang': 10,
 'Sorong': 1,
 'Ternate': 6,
 'Tual': 2}

In [136]: x = oc.keys()

In [137]: y = oc.values()

In [138]: col = list('rgbcmyk')

In [139]: plt
Out[139]: <module 'matplotlib.pyplot' from '/usr/lib/pymodules/python2.7/matplotlib/pyplot.pyc'>

In [140]: plt.scatter(x, y, color=colors.pop())
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-140-9146a68fb801> in <module>()
----> 1 plt.scatter(x, y, color=colors.pop())

NameError: name 'colors' is not defined

In [141]: plt.scatter(x, y, color=col.pop())
---------------------------------------------------------------------------
ValueError                                Traceback (most recent call last)
<ipython-input-141-58598719e9d3> in <module>()
----> 1 plt.scatter(x, y, color=col.pop())

/usr/lib/pymodules/python2.7/matplotlib/pyplot.pyc in scatter(x, y, s, c, marker, cmap, norm, vmin, vmax, alpha, linewidths, verts, hold, **kwargs)
   3085         ret = ax.scatter(x, y, s=s, c=c, marker=marker, cmap=cmap, norm=norm,
   3086                          vmin=vmin, vmax=vmax, alpha=alpha,
-> 3087                          linewidths=linewidths, verts=verts, **kwargs)
   3088         draw_if_interactive()
   3089     finally:

/usr/lib/pymodules/python2.7/matplotlib/axes.pyc in scatter(self, x, y, s, c, marker, cmap, norm, vmin, vmax, alpha, linewidths, verts, **kwargs)
   6335             self.set_ymargin(0.05)
   6336 
-> 6337         self.add_collection(collection)
   6338         self.autoscale_view()
   6339 

/usr/lib/pymodules/python2.7/matplotlib/axes.pyc in add_collection(self, collection, autolim)
   1479             len(collection._paths) and
   1480             len(collection._offsets)):
-> 1481             self.update_datalim(collection.get_datalim(self.transData))
   1482 
   1483         collection._remove_method = lambda h: self.collections.remove(h)

/usr/lib/pymodules/python2.7/matplotlib/collections.pyc in get_datalim(self, transData)
    183             transOffset = transOffset.get_affine()
    184 
--> 185         offsets = np.asanyarray(offsets, np.float_)
    186         if np.ma.isMaskedArray(offsets):
    187             offsets = offsets.filled(np.nan)

/usr/lib/python2.7/dist-packages/numpy/core/numeric.pyc in asanyarray(a, dtype, order)
    510 
    511     """
--> 512     return array(a, dtype, copy=False, order=order, subok=True)
    513 
    514 def ascontiguousarray(a, dtype=None):

ValueError: could not convert string to float: Gorontalo

In [142]: plt.scatter(y, color=colors.pop())
---------------------------------------------------------------------------
NameError                                 Traceback (most recent call last)
<ipython-input-142-ec1d325a30ec> in <module>()
----> 1 plt.scatter(y, color=colors.pop())

NameError: name 'colors' is not defined

In [143]: plt.scatter(y, color=col.pop())
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-143-e58bceed0ceb> in <module>()
----> 1 plt.scatter(y, color=col.pop())

TypeError: scatter() takes at least 2 arguments (1 given)

In [144]: plt.plot(y, color=col.pop())
Out[144]: [<matplotlib.lines.Line2D at 0x7f43b089dad0>]

In [145]: plt.legend(oc.keys())
Out[145]: <matplotlib.legend.Legend at 0x7f43b089d890>

In [146]: plt.show()
Exception in Tkinter callback
Traceback (most recent call last):
  File "/usr/lib/python2.7/lib-tk/Tkinter.py", line 1489, in __call__
    return self.func(*args)
  File "/usr/lib/pymodules/python2.7/matplotlib/backends/backend_tkagg.py", line 276, in resize
    self.show()
  File "/usr/lib/pymodules/python2.7/matplotlib/backends/backend_tkagg.py", line 348, in draw
    FigureCanvasAgg.draw(self)
  File "/usr/lib/pymodules/python2.7/matplotlib/backends/backend_agg.py", line 451, in draw
    self.figure.draw(self.renderer)
  File "/usr/lib/pymodules/python2.7/matplotlib/artist.py", line 55, in draw_wrapper
    draw(artist, renderer, *args, **kwargs)
  File "/usr/lib/pymodules/python2.7/matplotlib/figure.py", line 1034, in draw
    func(*args)
  File "/usr/lib/pymodules/python2.7/matplotlib/artist.py", line 55, in draw_wrapper
    draw(artist, renderer, *args, **kwargs)
  File "/usr/lib/pymodules/python2.7/matplotlib/axes.py", line 2086, in draw
    a.draw(renderer)
  File "/usr/lib/pymodules/python2.7/matplotlib/artist.py", line 55, in draw_wrapper
    draw(artist, renderer, *args, **kwargs)
  File "/usr/lib/pymodules/python2.7/matplotlib/collections.py", line 718, in draw
    return Collection.draw(self, renderer)
  File "/usr/lib/pymodules/python2.7/matplotlib/artist.py", line 55, in draw_wrapper
    draw(artist, renderer, *args, **kwargs)
  File "/usr/lib/pymodules/python2.7/matplotlib/collections.py", line 254, in draw
    transform, transOffset, offsets, paths = self._prepare_points()
  File "/usr/lib/pymodules/python2.7/matplotlib/collections.py", line 227, in _prepare_points
    offsets = np.asanyarray(offsets, np.float_)
  File "/usr/lib/python2.7/dist-packages/numpy/core/numeric.py", line 512, in asanyarray
    return array(a, dtype, copy=False, order=order, subok=True)
ValueError: could not convert string to float: Gorontalo

In [147]: y
Out[147]: [1, 1, 2, 2, 1, 1, 2, 1, 10, 6, 1, 1, 1]

In [148]: plt.plot(oc.values())
Out[148]: [<matplotlib.lines.Line2D at 0x7f43b07ef850>]

In [149]: plt.show()

In [150]: plt.plot(oc.values())
Out[150]: [<matplotlib.lines.Line2D at 0x7f43b0670dd0>]

In [151]: plt.plot(oc.values())

KeyboardInterrupt

In [151]: plt.legend(oc.keys())
Out[151]: <matplotlib.legend.Legend at 0x7f43b0a8e290>

In [152]: plt.show()

In [153]: plt.bar(range(len(oc)), oc.values(), align=

In [153]: plt.bar(range(len(oc)), oc.values(), align='center')
Out[153]: <Container object of 13 artists>

In [154]: plt.xticks(range(len(oc)), oc.keys())
Out[154]: 
([<matplotlib.axis.XTick at 0x7f43b06abcd0>,
  <matplotlib.axis.XTick at 0x7f43b0756690>,
  <matplotlib.axis.XTick at 0x7f43b0724bd0>,
  <matplotlib.axis.XTick at 0x7f43b058ee90>,
  <matplotlib.axis.XTick at 0x7f43b059b610>,
  <matplotlib.axis.XTick at 0x7f43b059bd50>,
  <matplotlib.axis.XTick at 0x7f43b05254d0>,
  <matplotlib.axis.XTick at 0x7f43b0525c10>,
  <matplotlib.axis.XTick at 0x7f43b052f450>,
  <matplotlib.axis.XTick at 0x7f43b052fb90>,
  <matplotlib.axis.XTick at 0x7f43b0539310>,
  <matplotlib.axis.XTick at 0x7f43b0539a50>,
  <matplotlib.axis.XTick at 0x7f43b05431d0>],
 <a list of 13 Text xticklabel objects>)

In [155]: plt.show()


```
