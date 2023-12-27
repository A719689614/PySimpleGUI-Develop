import PySimpleGUI as sg 
menu =[
    ["file",['news','open','save','exit']],
    ["edit",['cancel','undo','crop','save','exit']],
    ["help",['update','about']]
    ]
layout = [[sg.Menu(menu)]]
window = sg.Window("AC_FUN",layout)

while True:
    event ,values = window.read()

    if event == None:
        break
window.close()