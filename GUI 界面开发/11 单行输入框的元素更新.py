import PySimpleGUI as sg
layout = [
    # [[sg.T(i)] for i in ['a','b', 'c', 'd'] ],
        #   [[[sg.In(i, key=i )] for i in range(3)]],
          [[sg.T(i), sg.In(i, key=i)] for i in '12345'],
          [sg.B('sure'), sg.B('cancel'),sg.B('update'),sg.B('refresh')]
]

window = sg.Window(title='PySimple', layout=layout)
event = None
values = None
while True:
    event, values = window.read()

    if event == None:
        break
    if event == 'cancel':
        break
    if event == 'update':
        window['1'].SetFocus()   # 用于更新元素的焦点
        window['1'].set_focus('TODO')  # TODO
        window['2'].update(
            value = '1',          # str: 更新输入框内的文本
            disabled = False,     # bool: 更新元素的禁用状态
                                  # 如果为True,输入框变成只读状态，无法写入.
            select = None,        # bool: 元素选中,如果为True,输入框内的文本被全选中
                                  # 和focus或者set_focus 一起使用
            visible = True,       # bool:更新元素的可见状态
            text_color = None,    # str: 更新输入框内的文本颜色
            background_color = None, # str: 更新输入框的背景颜色
            move_cursor_to = 'end'   # 光标移动文本的最后，和value_focus一起试着使用

        )
    elif event == 'refresh':
        window['2'].update(
            value = '2',          # str: 更新输入框内的文本
            disabled = False,     # bool: 更新元素的禁用状态
                                  # 如果为True,输入框变成只读状态，无法写入
            select = None,) # bool: 元素选中,如果为True,输入框内的文本被全选中

window.close()        
    

