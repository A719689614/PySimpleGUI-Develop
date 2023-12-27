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
           autoscroll=False,
           focus=False,
        
           )]
    ]

window = sg.Window("ac_fun",layout)
while True:
    event,values = window.read()
    if event == None:
        break
    if event =='cancel':
        sg.cprint('cancel','你按了取消',end=None,
                  sep=" ",
                  text_color=None,
                  background_color=None,
                  colors=None,
                  key=None,
                  justification=None,
                  )
window.close()