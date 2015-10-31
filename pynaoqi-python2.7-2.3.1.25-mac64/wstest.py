#!/usr/bin/env python
# -*- coding: utf-8 -*-

import websocket
import thread
import time
import json
from naoqi import ALProxy
robotIP = "192.168.10.74" 

def on_message(ws, message):
    print message
    receive=json.loads(message)
    print receive

    target_action = str(receive["Action"])
    target_data = str(receive["Txt"])
    print target_action
    print target_data
    
    tts = ALProxy("ALTextToSpeech", robotIP, 9559)
#    tts.setLanguage("Japanese")
    tts.setLanguage("English")
#    tts.setParameter("pitchShift", 1.5)
    tts.say(target_data)

def on_error(ws, error):
    print error

def on_close(ws):
    print "### closed ###"

def on_open(ws):
    command = json.dumps({'Action': '', 'Txt': 'I am Pepper!!'}, separators=(',',':'), ensure_ascii=False)
    ws.send(command)

if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://echo.websocket.org/",
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()
