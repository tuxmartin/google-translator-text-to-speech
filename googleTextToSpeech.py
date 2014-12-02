#! /usr/bin/python

# https://github.com/tuxmartin/google-translator-text-to-speech
# !!! Pouze pro vyukove ucely! Na 99,9% porusuje licenci Googlu !!!

"""
Pouziti:

	$ echo "test 123" | python googleTextToSpeech.py cs
	$ echo "test 123" | python googleTextToSpeech.py en

Pokud neni zadany jazyk, pouzije se cestina.

Je nutne mit nainstalovany "wget" a "madplay" prehravac!
http://packages.ubuntu.com/search?keywords=madplay
"""

import sys
from subprocess import call
import urllib

try:
	jazyk = sys.argv[1]	
	#print "Jazyk pro cteni = ", jazyk
except IndexError:
	jazyk = "cs"
	print "Nebyl zadan jazyk pro cteni! Pouzivam vychozi = ", jazyk

text = ""
for line in sys.stdin:
#	print line
	text += line		

cti = urllib.quote_plus(text)

userAgent = "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:30.0) Gecko/20100101 Firefox/30.0";
prikaz = "wget -q -U \"" + userAgent + "\" -O - \"http://translate.google.com/translate_tts?ie=UTF-8&tl="+ jazyk +"&q=" + cti + "\" | madplay -q -"
#print prikaz
call(["/bin/sh", "-c", prikaz])

