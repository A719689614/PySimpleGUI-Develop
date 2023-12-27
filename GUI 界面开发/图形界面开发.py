import PySimpleGUI as sg

layout = [[sg.Text("Please Input Your Name")],
          [sg.Text("name    :"), sg.Input()],
          [sg.Text("age     :"), sg.Input()],
          [sg.Text("gender  :"), sg.Input()],
          [sg.Text("amount  :"), sg.Input()],
          [sg.Text("password:"), sg.Input()],
          [sg.Button("sure"), sg.Button("cancel")]

          ]

window = sg.Window('Python GUI', layout)

while True:
    event, values = window.read()

    if event is None:
        break

window.close()
