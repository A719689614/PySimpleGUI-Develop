# import PySimpleGUI as sg
# layout = [
#           [sg.B(image_filename=r'D:\AC Center\Button.png',key='-button-'),]
#           ]


# window = sg.Window('AC_FUN',layout)
# while True:
#     event, values= window.read()
#     print(event)
#     if event == None:
#         break


# 图片编码格式
import base64
f = open(r'D:\AC Center\Button.png','rb')
res = f.read()
s = base64.b64encode(res)
f.close()

import PySimpleGUI as sg
layout = [
          [sg.B(image_data=s,key='-button-'),]
          ]


window = sg.Window('AC_FUN',layout)
while True:
    event, values= window.read()
    print(event)
    if event == None:
        break