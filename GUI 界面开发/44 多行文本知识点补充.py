# print方法
import  PySimpleGUI as sg
layout = [
    [sg.ML(default_text='AC',key='-text-')],
    [sg.OK(),sg.VerticalSeparator(
    color=None,key=None,pad=None,
)    ,sg.Cancel()],
    ]
window = sg.Window("AC_FUN",layout)
while True:
    event, values=window.read()
    if event == None:
        break
    if event == "OK":
        window['-text-'].print('hello world'
                               ,
                               end=None,
                               sep=None,
                               text_color=None,
                               background_color=None,
                               justification=None,
                               )
        
    if event == "Cancel":
        sg.cprint('cancel','you passed cancel')


window.close()