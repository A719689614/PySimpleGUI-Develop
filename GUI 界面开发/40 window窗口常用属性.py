import PySimpleGUI as sg

menu =[
    ["file",['news','open','save','exit']],
    ["edit",['cancel','undo','crop','save','exit']],
    ["help",['update','about']]
    ]
layout = [[sg.Menu(menu,)]]
window = sg.Window("AC_FUN",layout,
                   location=None,
                   size=(None,None),
                   element_padding=(None,None),
                   button_color=None,
                   font=(None,None),
                   background_color=None,
                   auto_close=None,
                   auto_close_duration=3,
                   no_titlebar=False,
                   grab_anywhere=False,
                   keep_on_top=False,
                   resizable=False,
                   disable_close=False,
                   disable_minimize=False,
                   right_click_menu=None,
                   transparent_color=None,
                   element_justification='center',

                   )

while True:
    event ,values = window.read()

    if event == None:
        break
window.close()