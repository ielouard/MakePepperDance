#!/usr/bin/env python2.7

import speech_recognition as sr
from os import path

audiofile="/home/ibrahim/projet_majeur/pepper/402.wav" # wav ou flac, pas de mp3




def transcription(audiofile):
	AUDIO_FILE = path.join(path.dirname(path.realpath(__file__)), audiofile)
	r = sr.Recognizer()
	with sr.AudioFile(AUDIO_FILE) as source:
	    audio = r.record(source)

	phrase=r.recognize_google(audio,language="fr-FR")
	return phrase

