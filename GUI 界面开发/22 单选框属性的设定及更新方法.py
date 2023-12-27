import PySimpleGUI as sg

a = ['非常满意', '满意', '一般','不满意']
layout = [
    [sg.T('请对该服务做出评价')],
    [sg.R(i,group_id=1,key=i)for i in a],
    [sg.B('确认',key='-B-')]
]

window = sg.Window('AC_FUN', layout)
while True:
    event,value= window.read()
    if event == None:
        break
    if event == '确认':
        window['满意'].update(value=True)

    if event == '-B-':
        print(value)
        for key in value:
            if value[key]== True:
                print(key)
            





window.close()



# 可更新元素
value =True,
text=None,
background_color=None,
text_color=None,
disabled=None,
visible=None,
    



    