import PySimpleGUI as sg

layout = [
    [sg.Text("Name   :"), sg.Input("input your name", key="Name")],
    [sg.Text("Age      :"), sg.Input("input your age", key="Age")],
    [sg.Text("Gender :"), sg.Input("input your gender", key="Gender")],
    [sg.Button("sure"), sg.Button("cancel")],
            ]

window = sg.Window(title='AC_Function', layout=layout)

while True:

    event, values = window.read()
    if event == None:
        break
    if event == 'sure':
        print(values)
    if event == 'cancel':
        break
    if event == 'sure':
        print(values['Name'])

window.close()

