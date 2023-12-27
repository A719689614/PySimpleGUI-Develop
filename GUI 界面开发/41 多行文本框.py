import  PySimpleGUI as sg
Text = "this is a simple"

layout = [
    [sg.ML(Text,
           enable_events=None,
           key=None,
           write_only=False,
           reroute_stdout=False,
           reroute_cprint=False,
           reroute_stderr=False,
           )]
    ]

window = sg.Window("ac_fun",layout)
while True:
    event,values = window.read()
    if event == None:
        break

window.close()