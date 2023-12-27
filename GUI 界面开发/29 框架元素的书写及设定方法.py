import PySimpleGUI as sg 
layout_1 = [
    [sg.T('账号'),sg.In()],
    [sg.T('密码'),sg.In()],
]
layout = [
    [sg.Frame(title='AC_FUN',
              layout=layout_1,
              title_color=None,
              title_location=None,
              background_color=None,
              relief=None,
              size=(None,None),
              font=None,
              pad=None,
              border_width=None,
              key=None,
              tooltip=None,
              right_click_menu=None,
              visible=True,
              )]
    
]


window = sg.Window("AC_FUN",layout)
while True:
    event,values =window.read()
    if event ==None:
        break
window.close()
