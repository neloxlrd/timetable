import speech_recognition as sr
import os
import sys
import webbrowser
from data import *


class Kesha:
    def __init__(self):
        print("Привет, чем я могу помочь вам?")
    # слушаю
    def listen(self):
        record = sr.Recognizer()
        with sr.Microphone() as microphone:
            print('Я Вас слушаю очень внимательно...')
            record.pause_threshold = 1
            record.adjust_for_ambient_noise(microphone, duration=1)
            audio = record.listen(microphone)
        try:
            cmd = record.recognize_google(audio, language="ru-RU").lower()
		    # вывод полученной команды
            print("Вы сказали: " + cmd)
            # Обработка ситуации если помошник ничего не понял
        except Exception as e:
		    # выводим сообщение об ошибке
            print("Я вас не понял, повторите")
            # заново ждём команду
            cmd = self.listen()
        return cmd

    # выполняю
    def doing(self, cmd):
        if 'останавись' in cmd:
            print("Да, конечно, без проблем")
            sys.exit()
        elif 'имя' in cmd:
            print("Меня зовут Кеша")
        elif 'расписание' in cmd:
            print(raspisanie)
        

if __name__ == '__main__':
    voice_helper = Kesha()
    while True:
        voice_helper.doing(voice_helper.listen())

