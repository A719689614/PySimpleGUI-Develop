import PySimpleGUI as sg

x = print(sg.theme_list())
# 查看主题颜色
y = sg.theme('LightGrey2')
# 调出弹窗
sg.popup('LightGrey')

# 打印按钮颜色
button = sg.theme_button_color()
print(button)

# 修改按钮文字颜色
sg.theme_button_color(('black','#d4d7dd'))
sg.popup('button')