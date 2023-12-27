import PySimpleGUI as sg
layout = [
    [sg.FileBrowse(button_text='Browse',
                   target=None,
                   file_types=None,
                   initial_folder=None,
                   ),sg.In()]
]

window = sg.Window("ac_fun",layout)

while True:
    event,values = window.read()
    if event == None:
        break


window.close()