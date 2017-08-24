#!/usr/bin/env python2
# -*- coding: utf-8 -*-
#
#

"""
I.N.T.E.A.X listen and do your orders with this script.Part of a I.N.T.E.A.X PROJECT. 
"""

__author__ = "Fexyler"
__date__   = "20.08.2017"
__thanksto__="Black Viking"

import os
import pyaudio
import speech_recognition as sr

r = sr.Recognizer()

a = 0

def STT():
	global a
	
	while True:		
		with sr.Microphone() as mic:
			if a == 0: 
				os.system("clear")
				a = a + 1
				return

			audio = r.listen(mic)

		try:
			result = r.recognize_google(audio,language="tr-TR")
			break
		except sr.UnknownValueError as e:
			continue
	return result.lower().strip()
