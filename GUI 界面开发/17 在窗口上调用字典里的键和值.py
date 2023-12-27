import PySimpleGUI as sg
dict = {'程序员1':'python','程序员2':'java','程序员3':'php','程序员4':'c++'}

list = []
for key in dict:
    # print(key)
    list.append(key)

layout = [
    [sg.LB(list,size=(20,10),font=('黑体',20),key='-LB-',enable_events=True)],
    [sg.T('INPUT'),sg.In('',size=(30),key='-IN-')]
]



window = sg.Window('AC_FUN',layout)

while True:
    event,values = window.read()
    if event == None:
        break
    if event == '-LB-':
        window['-IN-'].update(dict[values['-LB-'][0]])

window.close()
