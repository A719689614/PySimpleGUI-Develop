import PySimpleGUI as sg 

# syntax
# sg.slider()
event = None,
values = None,


layout = [
    [sg.Slider(range=(0,1000),
               size=(50,30),
               font = None,
               text_color='black',
               default_value=100,
               resolution=10,
               tick_interval=100,
               orientation=('vertical')
               )],\
]

window = sg.Window('AC_FUN', layout)
while True:
    event, values = window.read()
    if event is None:
        break

window.close()