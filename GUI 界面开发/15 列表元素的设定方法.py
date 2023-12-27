import PySimpleGUI as sg

list = ['python','javascript','c++','php','html']

layout = [
    [sg.Listbox(list,
                default_values=None,              # 默认选中的值或者列表
                key=None,                         # 元素的唯一标识符
                select_mode=None,                 # 选择模式，有效值包含如下4种。
                                                  # single 单选，更换时点击选择
                                                  # multiple , 可以多选，逐一点击选择
                                                  # browse ,单选，鼠标按住也可以更换选择
                                                  # extended ,可以多选，鼠标按住可以扩展选择
                enable_events=False,              # 元素的事件属性
                                                  # 如果设定为True,元素列表项目被选中是会发生事件.
                bind_return_key=False,            # 绑定回车键
                size=(30,6),                      # 字符宽度,行高
                disabled=False,                   # 元素是否禁用
                auto_size_text=None,              # 如果为True,元素自动根据内容大小调整
                font=None,                        # 设置字体名称或者大小
                no_scrollbar=True,                # 如果设置为False则没有滚动条
                 )]
]

window = sg.Window('AC_FUN',layout)
while True:
    event,values=window.read()
    print(event)
    if event == None:
        break




window.close()