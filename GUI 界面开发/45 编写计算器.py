import PySimpleGUI as sg
def button(text):
    return sg.B(text,pad=(2,2),size=(4,2),button_color='black',font=('黑体',18))
layout=[
    [sg.T('AC_FUN计算器PYTHON编程',font=('黑体',12,),key='-show-')],
    [sg.In(size=(12,4),font=('黑体',28),key='-input-')],
    [button(i) for i in ['AC','(',')','%']],
    [button(i) for i in ['1','2','3','+']],
    [button(i) for i in ['4','5','6','-']],
    [button(i) for i in ['7','8','9','X']],
    [button(i) for i in ['0','.','=','÷']],
    ]

window = sg.Window('AC_FUN',layout,background_color='white')
while True:
    event, values = window.read()
    print(event)
    # print(values)
    if event == None:
        break 
    if event in ('0123456789+-().'):
        window['-input-'].update(values['-input-']+event)
    if event == 'X':
        window['-input-'].update(values['-input-']+'*')
    if event == '÷':
        try:
            window['-input-'].update(values['-input-']+'/')
        except:
            pass
                  
    if event == '%':
        try:
            window['-input-'].update(eval(values['-input-']+'/100'))
        except:
            window['-input-'].update('')
            sg.popup('%符号必须有数字表达式才能运行',
                     background_color='white',font=('黑体'),text_color='black',
                     button_color='black') 
        
    if event == '=':
        try:
            window['-input-'].update(eval(values['-input-']))
        except:
            window['-input-'].update('')
            sg.popup('除法分母不能为0',
                     background_color='white',font=('黑体'),text_color='black',
                     button_color='black') 

    if event == 'AC':
        window['-input-'].update('')

window.close()