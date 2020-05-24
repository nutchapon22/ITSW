import speech_recognition as sr
from time import ctime
import time
import os
from gtts import gTTS
import cv2

def speak(audioString):
    print(audioString)
    tts = gTTS(text=audioString, lang='th')
    os.system("nbot audio.mp3")
def recordAudio(): # อัดเสียง
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Say something!")
        audio = r.listen(source)
    data = ""
    try:
        data = r.recognize_google(audio,language="th")
        print("You said: " + data)
    except sr.UnknownValueError:
        print("Google Speech Recognition could not understand audio")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    
    return data
 
def itsw(data):
    if "กิน" in data:
        img = cv2.imread("eat.jpg",cv2.IMREAD_COLOR)
        cv2.imshow('Image',img)
        cv2.waitKey(800)
        cv2.destroyAllWindows()
    
    if "สวัสดี" in data:
        img = cv2.imread("hello.jpg",cv2.IMREAD_COLOR)
        cv2.imshow('Image',img)
        cv2.waitKey(800)
        cv2.destroyAllWindows()
    
    if "ฉัน" in data:
        img = cv2.imread("me.jpg",cv2.IMREAD_COLOR)
        cv2.imshow('Image',img)
        cv2.waitKey(800)
        cv2.destroyAllWindows()
    
    if "ชอบ" in data:
        img = cv2.imread("like.jpg",cv2.IMREAD_COLOR)
        cv2.imshow('Image',img)
        cv2.waitKey(800)
        cv2.destroyAllWindows()
    
    if "ขอโทษ" in data:
        img = cv2.imread("sorry.jpg",cv2.IMREAD_COLOR)
        cv2.imshow('Image',img)
        cv2.waitKey(800)
        cv2.destroyAllWindows()
    
    if "หิว" in data:
        img = cv2.imread("hungry.jpg",cv2.IMREAD_COLOR)
        cv2.imshow('Image',img)
        cv2.waitKey(800)
        cv2.destroyAllWindows()
    
    if "เกม" in data:
        img = cv2.imread("game.jpg",cv2.IMREAD_COLOR)
        cv2.imshow('Image',img)
        cv2.waitKey(800)
        cv2.destroyAllWindows()
    
    if "กระหาย" in data:
        img = cv2.imread("nwater.png",cv2.IMREAD_COLOR)
        cv2.imshow('Image',img)
        cv2.waitKey(800)
        cv2.destroyAllWindows()

    if "วิ่ง" in data:
        img = cv2.imread("run.jpg",cv2.IMREAD_COLOR)
        cv2.imshow('Image',img)
        cv2.waitKey(800)
        cv2.destroyAllWindows()

    if "อิ่ม" in data:
        img = cv2.imread("full.jpg",cv2.IMREAD_COLOR)
        cv2.imshow('Image',img)
        cv2.waitKey(800)
        cv2.destroyAllWindows()
         
# เริ่มต้นการทำงาน

time.sleep(2)
speak("Speak something")

while 1:
    data = recordAudio()
    itsw(data)