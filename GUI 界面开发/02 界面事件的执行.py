import PySimpleGUI as sg


layout = [[sg.Text("界面测试",enable_events=True), sg.Input()],
          [sg.Text("测试"), sg.Input()],
          [sg.Text("测试"), sg.Input()],
          [sg.Text("测试"), sg.Input()],
          [sg.Button("确认"), sg.Button("取消")]]

window = sg.Window("啊程测试图形界面", layout)

while True:

    event, values = window.Read()
    # default 
    # if event == None:
    #     break
    
    # 方法一
    # if event == "确认":
    #     sg.Popup("点击确认关闭窗口")
    #     break
    
    # 方法二
    # if event in ("确认", None):
    #     sg.Popup("点击确认关闭窗口")
    #     break
    
    # 方法三
    if event.startswith("确认"):
        sg.Popup('确认关闭窗口')
        break
    if event.endswith("取消"):
        sg.Popup("取消关闭窗口")
        break
    if event == "界面测试":
        sg.Popup("点击无效")
        continue
window.close()

