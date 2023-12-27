import PySimpleGUI as sg

# layout =[[sg.Text(i)for i in '请输入您的信息'],
#          [[sg.Text(i)] for i in ['姓名','性别','年龄']],
    
#         [sg.Button("确定"),sg.Button("返回")]

#           ]

# window = sg.Window('AC_FUN',layout=layout)
# while True:
#     event,values = window.read()
#     if event == None:
#         break
#     if event == '确定':
#         continue
#     if event == '返回':
#         break



    # 元素和布局的另一种组合方式
def create(any):
    layout=[[sg.Text("please input your information")],
        [sg.Text('name')]+[sg.In()]]+[[sg.Text('gender')]+[sg.In()]]+[[sg.Text('age')]+[sg.In()]],[sg.Button(button_text='sure')
        ,sg.B('cancel')],
    
    print(sg.theme_list())
    sg.theme('LightBlue5')
    sg.theme_button_color(color='#082567')
    sg.theme_border_width(2)

            

    window = sg.Window(title='AC_FUN',layout=layout)
    while True:
            event,values = window.read()
            if event == None:
                break
            if event == 'sure':
                continue
            if event == 'cancel':
                break

create(any)






