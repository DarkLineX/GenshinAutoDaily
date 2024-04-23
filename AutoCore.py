import time

from airtest.core.api import device, keyevent

import UtilTouch
import UtilsThread


def whereByText(text):
    if '游戏前详阅' in text:
        print('游戏加载警告页面')
        return 0
    elif '抵制不良游戏' in text and '自律公约' in text:
        print('游戏加载首页')
        return 0
    elif 'CNRELWin' in text and '输入密码' in text:
        print('登录掉了 需要重新登录')
        return 0
    elif 'CNRELWin' in text and '点击进入':
        print('等待进入游戏 需要点击')
        return 1
    else:
        print('不知道在什么界面了 当前文字 ' + text)
        return -1


def intoGame():
    # 点击进入
    width, height = device().get_current_resolution()
    UtilTouch.airtest_touch_point(width / 2, height / 2, '点击计入游戏', 3)
    UtilsThread.threadSleep(15, '等待游戏加载进入')

    # 领取月卡
    UtilTouch.airtest_touch_point(width / 2, height / 2, '月卡1', 3)
    UtilTouch.airtest_touch_point(width / 2, height / 2, '月卡2', 3)
    UtilTouch.airtest_touch_point(width / 2, height / 2, '月卡3', 3)

    # 领取邮件
    keyevent('{ESC}')
    time.sleep(2)
    UtilTouch.airtest_touch_point(41,453, '点开邮件', 3)
    UtilTouch.airtest_touch_point(176,725, '全部领取', 3)

    keyevent('{ESC}')
    time.sleep(2)
    keyevent('{ESC}')
    time.sleep(2)
    keyevent('{F3}')
    time.sleep(2)



    ## 直接关机
    # killGame()







