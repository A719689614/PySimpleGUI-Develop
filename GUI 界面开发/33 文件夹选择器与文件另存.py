import PySimpleGUI as sg
layout = [
    [sg.FileBrowse(button_text='Browse'),sg.In()],
    [sg.FilesBrowse(button_text='Folder'),sg.In()],
    [sg.FileSaveAs(button_text='save as'),sg.In()]
    ]



window = sg.Window("ac_fun",layout)

while True:
    event, values = window.read()
    print(event)
    if event == None:
        break

window.close()


# attributes

button_text =None,
target = None,
file_type = None,
initial_folder = None,