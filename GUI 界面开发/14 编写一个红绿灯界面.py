import PySimpleGUI as sg 
layout =[
    [sg.B('红灯',button_color=('black','red'),key='-red-',size=(30,10))],
    [sg.B('绿灯',button_color=('black','green'),key='-green-',size=(30,10))],
    [sg.B('黄灯',button_color=('black','yellow'),key='-yellow-',size=(30,10))]
]

window = sg.Window('AC_FUN',layout)
while True:
    event, values = window.read()
    print(event)
    if event == None:
        break
    if event == '-red-':
        window['-red-'].update(button_color=('black','red'))
        window['-green-'].update(button_color=('black','grey'))
        window['-yellow-'].update(button_color=('black','grey'))
    if event == '-green-':
        window['-red-'].update(button_color=('black','grey'))
        window['-green-'].update(button_color=('black','green'))
        window['-yellow-'].update(button_color=('black','grey'))
    if event == '-yellow-':
        window['-red-'].update(button_color=('black','grey'))
        window['-green-'].update(button_color=('black','grey'))
        window['-yellow-'].update(button_color=('black','yellow'))

window.close()