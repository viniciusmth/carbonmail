import speech_recognition as sr

def ouvir():

    mic = sr.Recognizer()

    with sr.Microphone() as source:

        mic.adjust_for_ambient_noise(source)
        print('Fale Algo...')
        audio = mic.listen(source)
    try:
        frase = mic.recognize_google(audio, language='pt-BR')
        print(f'Você disse: {frase}')
    except sr.UnknownValueError:
        print('Não entendi')
        

    return frase

ouvir()