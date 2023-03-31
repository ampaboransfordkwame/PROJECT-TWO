import PySimpleGUI as sg
import pyttsx3

text_to_speech_engine = pyttsx3.init()
voice_types = text_to_speech_engine.getProperty('voices')

layout = [[sg.Text('Select the type of voice:', text_color='white', background_color='black'),
           sg.Radio('Male', 'RADIO1', default=True, key='male', background_color='black'),
           sg.Radio('Female', 'RADIO1', key='female', background_color='black')],
          [sg.Text('Enter text to speak:', text_color='white', background_color='black')],

          [sg.InputText(key='input_user'), sg.Button('Speak', button_color='red')],

          ]

window = sg.Window('RANSFORD_PROJECT2', layout, background_color='black')

while True:
    event, values = window.read()
    if event == sg.WINDOW_CLOSED:
        break
    elif event == 'Speak':
        text = values['input_user']
        if values['male']:
            text_to_speech_engine.setProperty('voice', voice_types[0].id)
        elif values['female']:
            text_to_speech_engine.setProperty('voice', voice_types[1].id)

            text_to_speech_engine.say(text)
            text_to_speech_engine.runAndWait()
            window.close()
