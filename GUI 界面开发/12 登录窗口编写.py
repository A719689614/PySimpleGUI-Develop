import PySimpleGUI as sg
User1 = {'用户名':'abc', '密码':'123'}
User2 = {'用户名':'def', '密码':'456'}

userlist = [User1, User2]

layout = [[sg.T('用户名',size=(10,None), font=('黑体')), sg.In("请输入您的用户名",tooltip='账户为英文字母',key='amount')],
          [sg.T('密码   ',size=(10,None), font=('黑体')), sg.In(default_text=' ',tooltip='密码为三位数字',key='password',password_char='*')],
          [sg.B('确认', font=('黑体')), sg.B('取消', font=('黑体')), sg.B('测试', font=('黑体'))]
          ]

window = sg.Window('simple', layout)
event = None
values = None
while True:
    event, values = window.read()
    if event == None:
        break
    if event == '取消':
         break
    if event == '确认':
        for user in userlist:
            if values['amount'] == user['用户名'] and values['password'] == user['密码']:
                sg.Popup('输入正确，正在登录账号')
                break
            else:
                sg.Popup('输入错误，请检查账户和密码')
                break

    if event == '测试':
        print(values['amount'],values['password'])        

window.close()
