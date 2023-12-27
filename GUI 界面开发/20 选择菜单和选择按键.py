"""
选择菜单
书写方法:sg.OptionMenu()
此元素和设置了只读属性的ComboBox很像.
它没有'font'属性,不可以设定字体样式和大小
没有'enable_events'事件属性,不可以触发事件
"""

default_value=None,                         # initial value 默认选中
key=None,                                   # 唯一标识符
size=(30,6),                                # 元素宽度,行高
auto_size_text=None,                        # 元素根据文本自动调节
background_color=None,                      # 背景颜色设定
text_color=None,                            # 文本颜色设定
enable_events=False,                        # 元素事件属性,如果设定为True,当元素被选中时,会发生一个时间
disabled=False,                             # 元素禁用状态设定,#设定为True时,元素不能进行选择,也不能输入
pad=None,                                   # 元素间隔设定                
tooltip=None,                               # str: 悬浮文本设定
readonly=False,                             # 元素只读属性,只能选择,不能输入内容.
font=None,                                  # 元素字体名称或者大小设定
visible=True,                               # 元素可见状态设定  



# 选择菜单可更行的属性
value = None,                            # 更新默认选中的元素
values = None,                           # 更新所有显示的文本选项
disable = None,                          # 更新元素的禁用状态
visible = None,                          # 更新元素的可见状态

"""
旋转按钮
书写方法:sg.Spin()
特征:含有向上向下两个箭头按钮
"""
# 旋转按钮可设定的属性
initial_value = None,                     # 默认显示选项
key = None,                               # 唯一标识符
disable = False,                          # 更新元素的禁用状态
enable_events = False,                    # 事件属性
size = (None,None),                       # 元素的宽度跟行高
auto_size_text = None,                    # 元素根据文本自动调节
font = None,                              # 字体的样式跟大小
background_color = None,                  # 背景颜色
text_color = None,                        # 文本颜色
pad = None,                               # 元素间隔设定
tooltip = None,                           # str: 悬浮文本设定
visible = True,                           # 元素的可见状态


# 旋转按钮可更行的属性
value = None,                            # 更新默认选中的元素
values = None,                           # 更新所有显示的文本选项
disable = None,                          # 更新元素的禁用状态
visible = None,                          # 更新元素的可见状态


import PySimpleGUI as sg

a = ['python', 'java', 'c++','php','html']
layout = [
    [sg.T('OptionMenu'),sg.OptionMenu(a,key='-OM-'),sg.T('Spin'),sg.Spin(a,key='-SP-',enable_events=True)],
    [sg.T('INPUT'),sg.In(key='-IN-')],
]



window = sg.Window('AC_FUN', layout)
while True:
    event, values = window.read()
    print(event)
    if event == None:
        break
    if event == '-SP-':
        window['-IN-'].update(values['-SP-'])
        print(values['-SP-'])
    if event == '-OM-':
        window['-IN-'].update(values['-OM-'])
        print(values['-OM-'])
