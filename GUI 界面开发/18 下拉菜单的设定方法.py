import PySimpleGUI as sg
# sg.Combo()
# sg.InputCombo()
# sg.DropDown()
# sg.Drop()
# Combo和Listbox最大的区别在于，可以输入，但是不能多选。
# Listbox取得的值是存放在列表里面，但是Combo取得的值是对象本身
dict = {'程序员1':'python','程序员2':'java','程序员3':'php','程序员4':'c++'}

list = []
for key in dict:
    # print(key)
    list.append(key)

layout = [
    [sg.Drop(list,
             default_value='java',                       # initial value 默认选中
             key=None,                                   # 唯一标识符
             size=(30,6),                                # 元素宽度,行高
             auto_size_text=None,                        # 元素根据文本自动调节
             background_color=None,                      # 背景颜色设定
             text_color=None,                            # 文本颜色设定
             enable_events=False,                        # 元素事件属性,如果设定为True,当元素被选中时,会发生一个事件
             disabled=False,                             # 元素禁用状态设定,设定为True时,元素不能进行选择,也不能输入
             pad=None,                                   # 元素间隔设定                
             tooltip=None,                               # str: 悬浮文本设定
             readonly=False,                             # 元素只读属性,只能选择,不能输入内容.
             font=None,                                  # 元素字体名称或者大小设定
             visible=True,                               # 元素可见状态设定       
    )]
]

window = sg.Window('AC_FUN', layout)
while True:
    event, values = window.read()
    print(event)
    if event == None:
        break