import speech_recognition as sr
import pyaudio
import pyttsx3
import webbrowser
import library
# import os    # for os.startfile("filename")
# import google.generativeai as genai
import gemini_client

rec=sr.Recognizer()
# genai.configure(api_key="AIzaSyADSpASVc0gsvwfaviDwPzM7iHmlbtZikE")
# model=genai.GenerativeModel("gemini-2.5-flash")
my_model=gemini_client.gemini_model("gemini-2.5-flash")

def process_command(command):
    
    if(command.lower().startswith("open")):
       site=command.lower().split(" ")[1]
       webbrowser.open(library.websites[site])
    elif (command.lower().startswith("play")):
       video=command.lower().split(" ")[1]
       webbrowser.open(library.coding[video])
    else:
       ai_request(command)

def ai_request(command):
   prompt= f"""Act like a virtual assistant named Jarvis. You are skilled in giving short educational
   tutorials on different subjects. Provide only 3-4 lines in response. My question is: {command}"""
   # response=model.generate_content(prompt)
   response=my_model.model.generate_content(prompt)
   output=response.text.strip()
   print(output)
   ai_speak(output)
def ai_speak(output):
   ai_engine=pyttsx3.init()
   ai_engine.say(output)
   ai_engine.runAndWait()

def speak(line):
   engine=pyttsx3.init()
   engine.say(line)
   engine.runAndWait()



while(True):
    print("Listening...")

    with sr.Microphone() as source:
        try:
           audio=rec.listen(source,timeout=4,phrase_time_limit=3)
        except Exception as e:
           print(e)
           continue
    try:  
     word=rec.recognize_google(audio)
    except Exception as e:
     print(e)
     continue

    if("jarvis" in word.lower()):
      print("Jarvis Activated")
      speak("Give command" )
      with sr.Microphone() as source:
        try:
           audio=rec.listen(source,timeout=2,phrase_time_limit=4)
        except Exception as e:
           print(e)
        try:    
          command=rec.recognize_google(audio)
          process_command(command)
        except Exception as e:
         print(e)
    elif(word.lower()=="go back"):
       print("THANKS FOR USING.")
       break
    else:
       print(word)





