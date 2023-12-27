import PySimpleGUI as sg 
# syntax
# sg.Image(filename='file/path/to/*.png')
filepath = r'D:\AC Center\Picture\humans\ComfyUI_00020_.png'
layout = [
    [sg.Image(filepath)]
    ]
# 支持for 循环遍历图片命名
# image=r'D:\AC Center\Picture\humans\'
# f'{i}' for i in range(1,4)


window = sg.Window('AC_FUN',layout)
while True:
    event,values = window.read()
    if event == None:
        break
window.close()
