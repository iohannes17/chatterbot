import pyttsx3

luna = pyttsx3.init()

sound = luna.getProperty('voices')
luna.setProperty('voice',sound[16].id)

luna.setProperty('rate',150)
luna.setProperty('volume',5)

