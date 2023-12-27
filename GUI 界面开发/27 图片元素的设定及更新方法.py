import PySimpleGUI as sg 
# syntax
# sg.Image(filename='file/path/to/*.png')
filepath = r'D:\AC Center\Picture\humans\ComfyUI_00020_.png'
layout = [
    [sg.Image(filepath,
              filename=None,                               # 图片路径
              data=None,                                   # base64编码字符串
              background_color=None,                       # 背景颜色设定
              size=(None,None),                            # 图片宽高设定
              pad=None,                                    # 元素间隔设定
              key=None,                                    # 元素唯一标识符
              tooltip=None,                                # 元素悬浮文本
              right_click_menu=None,                       # 右击调出菜单
              visible=None,                                # 元素可见状态
              enable_events=False,                         # 元素的事件属性                                   
              )]
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


# 更新方法及可更新元素
# 语法
# window[key].update()