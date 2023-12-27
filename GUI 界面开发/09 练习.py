import PySimpleGUI as sg

layout = [[sg.B('中文'),sg.B('ENGLISH')],
          [sg.T('请输入你的信息', key='0')],
          [sg.T('姓名', key='1', size = (8,1)),sg.In()],
          [sg.T('性别', key='2', size = (8,1)),sg.In()],
          [sg.T('年龄', key='3', size = (8,1)),sg.In()],
          [sg.B('确认', key='4'),sg.B('取消', key='5')]

]
window = sg.Window('AC_FUN', layout)
event = None
values = None
while True:
    event, values = window.read()
    print(event)
    if event == None:
        break
    if event == 'ENGLISH':
        window['0'].update('please input your info')             
        window['1'].update('Name')               
        window['2'].update('Sex')               
        window['3'].update('Age')               
        window['4'].update('Sure')              
        window['5'].update('Cancel')
    elif event == '中文':
        window['0'].update('请输入你的信息')             
        window['1'].update('姓名')               
        window['2'].update('性别')               
        window['3'].update('年龄')               
        window['4'].update('确认')              
        window['5'].update('取消')
    else:
        pass
                  
window.close()
