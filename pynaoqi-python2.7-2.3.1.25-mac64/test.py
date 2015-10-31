#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import time

from naoqi import ALProxy
robotIP = "192.168.10.74" 

memory = ALProxy("ALMemory", robotIP, 9559)

############
# motion #
############
motion = ALProxy("ALMotion", robotIP, 9559)
#motion.wakeUp()
motion.moveInit()
motion.rest()
#motion.moveTo(0.5, 0, 0)
#motion.post.moveTo(0.5, 0, 0)


############
# Speech #
############
tts  = ALProxy("ALTextToSpeech", robotIP, 9559)
tts.setLanguage("Japanese")
#tts.setParameter("speed", 0.5)
tts.setParameter("pitchShift", 1.0)
#tts.say("ぼくは、ペッパー")

############
# Speech Recognition #
############
asr = ALProxy("ALSpeechRecognition", robotIP, 9559)
asr.setLanguage("Japanese")
asr.pause(True)

vocabulary = ["こんにちは", "ペッパー"]
asr.setVocabulary(vocabulary, False)
print 'Speech recognition engine started'
time.sleep(20)

# Start the speech recognition engine with user Test_ASR
asr.subscribe("Test_ASR")
#while True:
sayData = memory.getData("WordRecognized")
print sayData
if sayData == "こんにちは":
    tts.say("こんにちは。ぼくは、ペッパー")
    
asr.unsubscribe("Test_ASR")
        

############
# Posture #
############
try:
    postureProxy = ALProxy("ALRobotPosture", robotIP, 9559)
except Exception, e:
    print "Could not create proxy to ALRobotPosture"
    print "Error was: ", e
    
#postureProxy.goToPosture("Crouch",0.8)
#postureProxy.goToPosture("StandInit", 1.0)
#print postureProxy.getPostureFamily()

