import os
import pyttsx3
import speech_recognition as sr
import webbrowser
import wikipedia
import datetime

audio = sr.Recognizer()
maquina = pyttsx3.init()
maquina.say('Olá, eu sou jarvis')
maquina.say('Como posso ajudar?')
maquina.runAndWait()

def executa_comando():
    try:
        with sr.Microphone() as source:
            print('Ouvindo..')
            voz = audio.listen(source)
            comando = audio.recognize_google(voz, language='pt-BR')
            comando = comando.lower()
            if 'Jarvis' in comando:
                comando = comando.replace('jarvis', '')
                maquina.say(comando)
                maquina.runAndWait()
        
        
    except:
        print('Microfone não está ok')
        
    return comando    

def comando_voz_usuario():
    comando = executa_comando()
    if 'horas' in comando:
        hora = datetime.datetime.now().strftime('%H:%M')
        maquina.say('Agora são ' + hora)
        maquina.runAndWait()
    elif 'procure por' in comando:
        procurar = comando.replace('procure por', '')
        wikipedia.set_lang('pt')
        resultado = wikipedia.summary(procurar,2)
        print(resultado)
        maquina.say(resultado)
        maquina.runAndWait()
comando_voz_usuario()