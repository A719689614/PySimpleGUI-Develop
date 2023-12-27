import PySimpleGUI as sg
mouth = ['january','february','march','april','may','jun','july','august','september','november','october','december']
week  = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']

layout = [
    [sg.ColorChooserButton(button_text='color choices'),sg.In()],
    [sg.CalendarButton(button_text='calendar'),sg.In()],
    ]
window = sg.Window("AC_FUN",layout)


while True:
    event, values = window.read()
    if event is None:
        break

window.close()


# main function

close_when_date_chosen = False,        # 选择日期后日历界面关闭

# 默认值设定
default_date_M_d_y = (1.3/2022),       # 默认值设定

# 区域设定
locale = None,

# 显示格式
format = "%Y-%m-%d%H:%M:%S",

# 指定日历显示的第一列
begin_at_sunday_phes=0,

# 指定月份的文本列表
month_names = None,

# 指定周几的文本列表、
day_abbreviations = None,

# 选择窗口的标题
title = "choose Date",

# 不显示标题
no_titlebar = False,

# 日历窗口的位置
location = (None,None)
