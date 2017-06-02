import argparse
from naoqi import ALProxy
import time
from transcrib import *

tts = audio = record = aup = None 

def main(robot_IP, robot_PORT=9559):
	global tts, audio, record, aup 
	# ----------> Connect to robot <----------
	tts = ALProxy("ALTextToSpeech", robot_IP, robot_PORT)
	audio = ALProxy("ALAudioDevice", robot_IP, robot_PORT)
	record = ALProxy("ALAudioRecorder", robot_IP, robot_PORT)
	aup = ALProxy("ALAudioPlayer", robot_IP, robot_PORT)
	# ----------> recording <----------

	record.stopMicrophonesRecording()
	print 'start recording...'
	record_path = '/home/nao/recordings/microphones/recording.wav'
	record.startMicrophonesRecording(record_path, 'wav', 16000, (0,0,1,0))
	time.sleep(3)
	record.stopMicrophonesRecording()
	print 'record over'

	print(transcription(record_path))
	# ----------> playing the recorded file <----------
	#fileID = aup.playFile("/home/nao/recordings/microphones/recording.wav")
	

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="192.168.1.34", help="Robot ip address")
    parser.add_argument("--port", type=int, default=9559, help="Robot port number")
    args = parser.parse_args()
	# ----------> main <----------
main(args.ip, args.port)
