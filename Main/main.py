from chatterbot import ChatBot  # method to train chatbot
from chatterbot.trainers import ListTrainer  # import chatbot
import os
import speech_handler as sphand
import speech_recognition as sr
from chatterbot.trainers import ChatterBotCorpusTrainer


bot = ChatBot('Tiberius')
bot.set_trainer(ChatterBotCorpusTrainer)
speech = sr.Recognizer()
#
# for _file in os.listdir('files'):
#     chats = open('files/' + _file, 'r').readlines()
#     bot.train(chats)

#
# bot.set_trainer(ChatterBotCorpusTrainer)
#
# # Train the chat bot with the entire english corpus
bot.train("chatterbot.corpus.english")




# name = input("Luna: What is your name? \n")
# sphand.luna.say('Welcome..................' + name)
# sphand.luna.runAndWait()


def speak_text_cmd(cmd):
    sphand.luna.say(cmd)
    sphand.luna.runAndWait()


def read_voice_cmd():
    voice_text = ''
    with sr.Microphone() as source:
        audio = speech.listen(source)

    try:
        voice_text = speech.recognize_google(audio)
    except sr.UnknownValueError:
        pass
    except sr.RequestError as e:
        print('Network error')
    return voice_text


if __name__ == '__main__':
    speak_text_cmd('Hello johnny....what shall we do today')
    while True:
        voice_note = read_voice_cmd()
        print('cmd: {}'.format(voice_note))

        if 'hello' in voice_note:
            speak_text_cmd('hello Sir')
            continue

        elif 'chat' in voice_note:
            request = read_voice_cmd()
            response = bot.get_response(request)
            sphand.luna.say(response)
            print ('Tiberius:',response, '  \n')
            sphand.luna.runAndWait()
            continue

        elif 'Goodbye' in voice_note:
            speak_text_cmd('Goodbye Sir. Have a lovely day')
            exit()

        else:
            speak_text_cmd('Sir, I am still training please give me another command')



#
# while True:
#     request = input(name +':')
#     response = bot.get_response(request)
#     sphand.luna.say(response)
#     print ('Luna:',response,'  \n') #prints the response or replies to the user
#     sphand.luna.runAndWait()
#
