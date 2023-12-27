# syntax
import PySimpleGUI as sg

layout_1 = [
    [sg.T('标题',font=('黑体',10))],
    [sg.In(font=('黑体',10))],
    [sg.T('作者',font=('黑体',10))],
    [sg.In('',font=('黑体',10))],
]

layout_2 = [
    [sg.ML('请输入正文内容',size=(30,20),font=('黑体',10))],
    [sg.B('确认',font=('黑体',12))],
]

layout=[
    [sg.Col(layout_1,
            background_color=None,                      # 整体背景颜色
            size=(None,None),                           # 元素宽高
            pad=(None,None),                            # 间隔设定
            scrollable=True,                            # 添加滚动条
            vertical_scroll_only=False,                 # 显示水平滚动条
            right_click_menu=None,                      # 右击调出菜单
            key=None,                                   # 元素唯一标识符
            visible=True,                               # 元素的可见状态
            justification='left'                        # 为列本身设置对齐方式
            ),sg.Col(layout_2),]
    ]

window = sg.Window('AC_FUN',layout)
while True:
    event,values = window.read()
    if event == None:
        break
window.close()