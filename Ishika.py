import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia
import pyjokes
import os
import smtplib

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty ('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()
def wishMe():
    hour = int(datetime.datetime.now().hour)
    if hour>=0 and hour<12:
        talk("Good Morning!     ")

    elif hour>=12 and hour<18:
        talk("Good Afternoon!      ")   

    else:
        talk("Good Evening!")  

    talk("Hello, I am Ishika. How May i help you?")




def take_command():
    try:
        with sr.Microphone() as source:
            print('listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice, language='en-in')
            command = command.lower()
            
    except Exception as e:   
        print("Say that again please...")  
        return "None"
    return command

def sendEmail(to, content):
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.login('Your Email id', 'Your Password')
    server.sendmail('senders email id', to, content)
    server.close()



if __name__ == "__main__":
    wishMe()
    while True:
        command = take_command()
        print(command)
        if 'play' in command:
            song = command.replace('play', '')
            talk('playing ' + song)
            pywhatkit.playonyt(song)
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            talk('Current time is ' + time)
        #elif 'send whatsapp message' in command:
            #pywhatkit.sendwhatmsg('Receivers mobile number', "Hello, this message is send by Virtual Assistant made by Aegis Students",19,10)
        elif 'whatsapp' in command:
            try:
                talk("Please say the number")
                content1 = '+91' + take_command()
                talk("What should I say?")
                content5 = take_command()
                pywhatkit.sendwhatmsg(content1, content5 ,17,10)   
                talk("Message has been sent!")
            except Exception as e:
                print(e)
                talk("Sorry Cant send the message")
        elif 'search' in command:
            person = command.replace('search', '')
            info = wikipedia.summary(person, 2)
            print(info)
            talk(info)
        elif 'date' in command:
            talk('sorry , I  have  a  headache')
        elif 'single' in command:
            talk('I am in a relationship with python')
        elif 'joke' in command:
            talk(pyjokes.get_joke())
        elif 'thank you' in command:
            talk('It has been my pleasure serving you')
        elif "who made you" in command or "who created you" in command: 
            talk("I  have  been  created  by  a  group  of  aegis  students.")
        elif "discuss" in command: 
            talk("We are going to discuss about my creation")

        elif 'email' in command:
            try:
                talk("What should I say?")
                content = take_command()
                to = "pranavdange0@gmail.com"    
                sendEmail(to, content)
                talk("Email has been sent!")
            except Exception as e:
                print(e)
                talk("Sorry Cant send the email") 
        else:
            print("Sorry, I didn't get you. ")
