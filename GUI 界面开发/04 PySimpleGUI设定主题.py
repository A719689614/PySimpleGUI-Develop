import PySimpleGUI as sg

sg.theme_previewer()
print(sg.theme_list())

sg.theme(new_theme='LightBlue')

sg.Popup('testing')


sg.theme('')

sg.Popup('testing')