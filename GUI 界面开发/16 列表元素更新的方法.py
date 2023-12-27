import PySimpleGUI as sg

list_1 = ['pythons', 'java','c++','php','html']
list_2 = ['程序员1', '程序员2','程序员3','程序员4','程序员5']

layout = [
    [sg.LB(list_1,size=(30,6),key='-list_1-',font=('黑体',20))], 
    [sg.B('编程语言',font=('黑体',20)),sg.B('程序员',font=('黑体',20))],
    [sg.B('set_to_index',font=('黑体',20))]
]

Window = sg.Window('AC_FUN',layout)
while True:
    event, values = Window.read()
    print(event)
    if event == None:
        break
    if event == '程序员':
        Window['-list_1-'].update(list_2)
    if event == '编程语言':
        Window['-list_1-'].update(list_1)
    if event == 'set_to_index':
        Window['-list_1-'].update(set_to_index=2)
       
