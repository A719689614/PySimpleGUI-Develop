import PySimpleGUI as sg
sg.Popup(
    title=None,                    # 弹窗标题
    button_color=None,             # 文本颜色
    background_color=None,         
    text_color=None,
    auto_close=None,
    auto_close_duration=3,
    custom_text=(None, None),       # 自定义按钮显示文本 
    non_blocking= False,           # 非阻塞设定
    font = None, 
    no_titlebar=None,
    grab_anywhere=False,           # 拖动界面
    keep_on_top=False,             # 置顶
    location=None,
    any_key_closes=False,          # 任意按键关闭
    image=None,
    modal=True,                    # 模态窗口
)