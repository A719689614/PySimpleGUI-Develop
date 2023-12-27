import PySimpleGUI as sg

layout = [[sg.T('账号',font=('黑体')),                                      
           sg.In('请输入您的账号',                                            # 默认值设定，可以为空字符
                 key = '-Input-',                                            # 元素的唯一标识符 规范
                 size=(None,None),                                           # 宽,行高
                 disabled=None,                                              # bool :元素禁用,如果为True则禁用，无法输入任何值
                 password_char='*',                                          # 密码字符,一般设置为*
                 justification='l',                                          # 对齐方式'l','r','c' 
                 background_color=None,                                      # 输入框的颜色
                 text_color = None,                                          # 输入框文本颜色
                 font=('黑体'),                                               # 输入框的字体名称和大小
                 tooltip=None,                                               # str:悬浮文本
                 border_width=None,                                          # 输入框边界线宽度设定
                 enable_events=False,                                        # boolean:输入框的时间属性
                                                                             # 如果设定为True,输入值时会发生一个时间
                 do_not_clear=True,                                          # bool :输入框内容不被清除，如果为False，一发生事件，该输入框内的值会被清除
                 focus=True,                                                # boolean:设定焦点，如果为True,则光标显示在此输入框内
                 pad=None,                                                  # 元素间隔
                 disabled_readonly_background_color=None,                   # str: 元素禁用时的背景颜色设定
                 disabled_readonly_text_color=None,                         # str:元素禁用时的文本设定颜色
                 right_click_menu=None,                                     # 右击按钮菜单List[List[Union[List[str],str]]],设定后,右击此元素会弹出菜单
                 visible=None,                                              # 元素的可见状态，如果为False,则界面不显示该元素
                             )],
         [sg.T('密码',font=('黑体')),sg.In(default_text='',focus=True)],
         [sg.B('确定',font=('黑体')),sg.B('返回',font=('黑体')),sg.B('关闭',font=('黑体'))]
          ]


Window = sg.Window('AC_FUN',layout)
event = None
values = None
while True:
    event, values = Window.read()
    print(event)
    if event == None:
        break
    if event == '关闭':
        break
    if event == '确定':
        print(Window['-Input-'])
