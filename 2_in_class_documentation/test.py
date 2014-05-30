# -*- coding: utf-8 -*-
"""
Created on Thu May 29 10:54:36 2014

@author: robertv
"""

import json
import urllib2

prefix="http://maps.googleapis.com/maps/api/geocode/json?address="
suffix="&sensor=false"
address="165%20Whitney%20Avenue,%20New%20Haven,%20CT"
url=prefix+address+suffix
fulladd="http://maps.googleapis.com/maps/api/geocode/json?address=8-10%20Broadway,%20London%20SW1H%200BG,%20United%20Kingdom&sensor=false"
j = urllib2.urlopen(url)
js = json.load(j)

type(js)

from pprint import pprint
pprint(js)

rstadd = js['results'][0]['address_components']

for rs in rstadd:
    print rs['short_name'], rs['types']

import pandas as pd
pd.DataFrame(rstadd)

print ourResult['lat'], ourResult['lng']


*** JSON - Loading
 
#+BEGIN_SRC python :results output code :session :exports result
jsn = """
    {"name":"batman",
     "hobbies": ["fast cars", "fast planes", "spending money"],
    "buddy":"robin",
    "enemies": [{"name":"The Joker"},
                {"name":"The People of Gotham"}]
                }
"""
import json
#NOTE: loads for strings, load for files
rslt = json.loads(jsn) #put this into a form for python
print rslt
jsn_again = json.dumps(rslt) #back to json
 #+END_SRC 

 #+RESULTS:
 #+BEGIN_SRC python
{u'buddy': u'robin', u'enemies': [{u'name': u'The Joker'}, {u'name': u'The People of Gotham'}], u'name': u'batman', u'hobbies': [u'fast cars', u'fast planes', u'spending money']}
 #+END_SRC

*** JSON - Converting to DataFrames

#+BEGIN_SRC python :results output code :session :exports result
enemies = pd.DataFrame(rslt['enemies'], columns=['name'])
enemies
#+END_SRC 

#+RESULTS:
#+BEGIN_SRC python
              name
0             The Joker
1             The People of Gotham

[2 rows x 1 columns]
#+END_SRC


*** JSON - Converting to DataFrames

#+BEGIN_SRC python :results output code :session :exports result
enemies = pd.DataFrame(rslt['enemies'], columns=['name'])
enemies
#+END_SRC 

#+RESULTS:
#+BEGIN_SRC python
              name
0             The Joker
1  The People of Gotham

[2 rows x 1 columns]
#+END_SRC

*** JSON - Example

#+BEGIN_SRC python :results output code :session :exports result
import json
import urllib2
import pprint import pprint
import pandas as pd

prefix="http://maps.googleapis.com/maps/api/geocode/json?address="
suffix="&sensor=false"
address="165%20Whitney%20Avenue,%20New%20Haven,%20CT"
url = prefix+address+suffix
j = urllib2.urlopen(url)
js = json.load(j)
type(js) #if in doubt, check type

#pprint(js) 

#notice nested list, so use index to get into it
rstadd = js['results'][0]['address_components']

for rs in rstadd:
    print rs['short_name'], rs['types']

import pandas as pd
pd.DataFrame(rstadd)
#+END_SRC 

urlencode()

urllib2.quote("test thing")



xml = """
    <root>
        <name type="superhero">Batman</name>
            <sidekick>Batty</sidekick>
        <contact type="email">riseup@batman.com</contact>
        <contact type="phone">555-1212</contact>
    </root>
            """

from lxml import objectify
root = objectify.fromstring(xml) #use parse from file

print root.tag
print root.text
print root.attrib

print root.name.tag
print root.name.text
print root.name.attrib

for con in root.contact:
    print con.text
    print con.attrib


 # loop over elements and print their tags and text
for chld in root.iterchildren():
        print "%s => %s" % (chld.tag, chld.text)

for chld in root.getchildren():
        print "%s => %s" % (chld.tag, chld.text)

http://lxml.de/1.3/tutorial.html
http://www.saltycrane.com/blog/2011/07/example-parsing-xml-lxml-objectify/

