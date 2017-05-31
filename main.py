
# -*- encoding: UTF-8 -*-


#------------------------- Bibliotheques ---------------------------#
import argparse
import time
import sys
from naoqi import ALProxy
import os
import threading

#------------------------- Fonctions ---------------------------#


def init(robotIP, PORT=9559):    #Initialisations des modules d'Aldebaran
    global motionProxy
    global tts
    global asr
    global memProxy
    global animatedSpeechProxy
    global touch
    global aup
    motionProxy = ALProxy("ALMotion", robotIP, PORT)
    tts = ALProxy("ALTextToSpeech", robotIP, PORT)
    asr = ALProxy("ALSpeechRecognition", robotIP, PORT)
    memProxy = ALProxy("ALMemory", robotIP, PORT)
    animatedSpeechProxy = ALProxy("ALAnimatedSpeech", robotIP, PORT)
    touch = ALProxy("ALTouch", robotIP, PORT) 
    aup = ALProxy("ALAudioPlayer", robotIP, PORT)

def playsound():
    aup.playFile("/home/nao/musique.mp3")

def listen():
    word=[]
    i=0
    while i<1:

	    asr.pause(True)
	    asr.setLanguage("French")
	    vocabulary = ["terminer","apprendre", "danser"]
	    asr.setVocabulary(vocabulary, False)
	    # Début de l'ASR
	    tts.say("Je peux soit te faire une petite danse mais tu peux aussi m'en apprendre une! Tu sais ce que tu aimerais ?")
	    asr.subscribe(robotIP)
	    print 'Speech recognition engine started'
	    memProxy.subscribeToEvent('WordRecognized',robotIP, 'wordRecognized')
	    asr.pause(False)
	    word=memProxy.getDataOnChange("WordRecognized",0)
	    asr.unsubscribe(robotIP)
	    asr.pause(True)
            print (word)
            if word[1]>0.4: i=2
    print (word)
    return word[0]

def touched():
	print (touch.getStatus()[9])
	return touch.getStatus()[9][1]

def stiffnessOff():
    stiffnames = ["Head","RArm", "LArm", "Leg"]
    stiffnessLists = 0.0
    timeLists = 1.0
    for i in range(3):
        motionProxy.stiffnessInterpolation(stiffnames[i], stiffnessLists, timeLists)

def stiffnessOn():
    stiffnames = ["Head","RArm", "LArm", "Leg"]
    stiffnessLists = 1.0
    timeLists = 1.0
    for i in range(3):
        motionProxy.stiffnessInterpolation(stiffnames[i], stiffnessLists, timeLists)


def getMouvement():
    stiffnessOff();
    tts.say('Tu mapprend un nouvo mouvement mon chat? ! touche moi la tête quand tu finis sil te plait')
    useSensors  = True
    names = "Body"
    sensorAngles=[] 
    print(int(touched()))
    while touched()==False:
        sensorAngles.append(motionProxy.getAngles(names, useSensors))
        time.sleep(0.1)
    tts.say('C fini')
    # Sauvegarde de la danse dans ALmemory et dans un fichier Excel
    file = open("danses.xls","w")
    file.write(str(sensorAngles)) 
    file.close
    memProxy.insertData("Danse1", sensorAngles)
    stiffnessOn()
    return sensorAngles

def doMouvement(mouvement):
    tts.say('je bouge')
    for i in range(0, len(mouvement)):
        changes = mouvement[i]
        fractionMaxSpeed = 0.2
        motionProxy.setAngles("Body", changes, fractionMaxSpeed)
        time.sleep(0.1)
    tts.say('Fini') 


#------------------------- MAIN ---------------------------#

def main():

    while True:
        if touched()==True: #toucher la tête pour démarrer
	    danse=[]
            motionProxy.wakeUp()
            tmp = threading.Thread(target=playsound)
            tmp.start()
	    global configuration 
            configuration= {"bodyLanguageMode":"random"}
            animatedSpeechProxy.say("Coucou toi ! je m'appelle Pépita! et oui je suis une vraie danseuse étoile !", configuration)

	    while True:  #Scénario
		global ordre
		ordre=listen()
	        tts.say("tu as dit " + ordre)
		if ordre=="apprendre":
			danse=getMouvement()
		elif ordre=="danser":
			danse = memProxy.getData("Danse1")
			if danse==[]:
		            animatedSpeechProxy.say("Apprend moi une danse d'abord !",configuration)
			else:
			    doMouvement(danse)
		if ordre=="terminer":
		         animatedSpeechProxy.say("Aurevoir !",configuration)
			 break;break;
	    motionProxy.rest()



if __name__ == "__main__":
    global robotIP
    global PORT
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="192.168.1.34",
                        help="Robot ip address")
    parser.add_argument("--port", type=int, default=9559,
                        help="Robot port number")

    args = parser.parse_args()
    robotIP=args.ip
    PORT=args.port
    init(robotIP, PORT)
    main()
