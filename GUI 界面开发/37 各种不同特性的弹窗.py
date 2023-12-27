import PySimpleGUI as sg
# 文件选择弹窗
result = sg.PopupGetFile("please browse your files")

# 没有标题的弹窗
sg.PopupAnnoying("",)

# 显示一段时间自动关闭弹窗
sg.PopupAutoClose("",)

# 弹窗含有一个cancelled按钮
sg.PopupCancel('',)

# 有ok和cancel两个按钮的弹窗
sg.PopupOKCancel('',)

# Error弹窗
sg.PopupError('',)

# 无按钮的弹窗
sg.PopupNoButtons('',)

# 显示弹出串口并立即返回
sg.popup_no_wait('',)