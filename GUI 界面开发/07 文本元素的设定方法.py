import PySimpleGUI as sg

text = '''江南春 唐 杜牧
千里莺啼绿映红，
水村山郭酒旗风。
南朝四百八十寺，
多少楼台烟雨中。'''
layout = [[sg.Text(text,
           key='-TEXT-',
           font=('黑体',15),
           size=(30,30),
           auto_size_text=True,
           enable_events=True,                                          # 
           relief="raised",                                             # 浮雕设计'raised','sunken
           border_width=10,
           text_color='yellow', 
           justification='center',                                      # 对其方式:'left','right','center'
           pad=None,                                                    # 
           right_click_menu=['1', ['1','2','3']],                       # 右击调出菜单 List[List[Union[List[Str],str]]],设定后，右击此元素可以调出菜单
           grab=None,                                                   # 如果为真，点此元素可以移动拖拽窗口
           tooltip= None,                                               # str: 悬浮文本，当光标置于该元素上方，会显示设定的文本
           visible=True                                                 # bool: 元素课件状态
           )
           ],
           [sg.B('sure'),sg.B('cancel')]
           ]
window = sg.Window('AC_FUN',layout=layout)
while True:
    event, values = sg.Window.read(self=window)
    if event == None:
        break
    if event == 'cancel':
        break
    if  event == 'sure':
        print(values)