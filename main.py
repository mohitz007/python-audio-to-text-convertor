# import sre_compile
import speech_recognition as sr
import os

dir = os.listdir()
r = sr.Recognizer()
for file in dir:
    if file.endswith(".wav"):
        with sr.AudioFile(file) as source:
            audio = r.record(source)
            try:
                # print("google thinks " + r.recognize_google(audio) + "\n \n \n \n")
                name = os.path.splitext(file)[0] + ".txt"
                # print(name)
                f = open( name , "w")
                f.write(r.recognize_google(audio))
                f.close()
            except sr.UnknownValueError:
                print("could not recognize")
            except sr.RequestError as e:
                print("google error; {0}".format(e))
