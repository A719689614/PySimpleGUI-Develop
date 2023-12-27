import PySimpleGUI as sg
# sg.PopupGetText(message='Test')

# result = sg.PopupGetText("please enter your password")
# print(result)

# example
pwd = '123'
list = [x for x in range(5)]
while True:
    result = sg.PopupGetText("Please enter your password")
    if result == pwd:
        break
    else:
        sg.Popup("reconfirm again")

# example
layout = [
    [sg.LB(list)]
    ]

Window = sg.Window("AC_FUN", layout)
while True:
    event,values = Window.read()
    if event == None:
        break
Window.close()