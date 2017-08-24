#!/usr/bin/env python2
# -*- coding: utf-8 -*-
# print "give me a bottle of code xd"
# ^ ^

"""
I.N.T.E.A.X can speak with this script.Part of a I.N.T.E.A.X PROJECT.
"""

__author__ = "Fexyler"
__date__   = "20.08.2017"
__thanksto__="Black Viking"

import pyttsx3

engine = pyttsx3.init()
engine.setProperty('voice', 'turkish')

def say(text):
	engine.say(text)
	engine.runAndWait()
	
