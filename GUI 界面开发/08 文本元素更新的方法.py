import PySimpleGUI as sg
layout = [
          [sg.T('程序员啊程',key='-Text-'),sg.B('点赞')]
]

window = sg.Window('AC_GUN',layout)

while True:
    event,value=window.read()
    print(event)
    if event==None:
        break
    if event=='点赞':
        window['-Text-'].update(
            value='谢谢支持!',                    # str 更新文本
            background_color="white",            # 更新文本背景颜色
            text_color=("black"),                # 更新文本颜色
            font=('黑体',30),                     # 更新字体的名称或者大小
            visible=None,                        # 更新元素的课件状态
        )

window.close()