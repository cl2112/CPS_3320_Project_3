import PySimpleGUI as sg

# layout = [
#     [sg.Text("Hello")],
#     [sg.Input()],
#     [sg.Button('OK')]
# ]

# window = sg.Window('This title!', layout)

# event, values = window.read()

# print('Hello', values[0], '! Thanks')

# window.close()

layout = [
    [sg.Text('What\'s your name?')],
    [sg.Input(key='-INPUT-')],
    [sg.Text(size=(40,1), key='-OUTPUT-')],
    [sg.Button('Ok'), sg.Button('Quit')]
]

window = sg.Window('Title here', layout)

while True:
    event, values = window.read()

    if event == sg.WINDOW_CLOSED or event == 'Quit':
        break

    if event == 'Ok':
        print('Ok Buttons pressed.')

    # window['-OUTPUT-'].update('Hello ' + values['-INPUT-'] + '! Thanks')

window.close()