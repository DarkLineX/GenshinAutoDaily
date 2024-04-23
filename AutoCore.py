import time

from airtest.core.api import device, keyevent

import UtilTouch
import UtilsThread
from UtilsPaddle import getTextPos, getPageText


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
        print('等待进入游戏 点击')
        return 1
    else:
        print('不知道在什么界面了 当前文字 ' + text)
        return -1


def intoGame():
    pos1 = getTextPos('点击进入')
    if pos1:
        cx = (pos1[0][0] + pos1[1][0]) / 2
        cy = (pos1[0][1] + pos1[2][1]) / 2
        UtilTouch.airtest_touch_point(cx, cy, '', 3)
        UtilsThread.threadSleep(30)

    # 领取月卡
    width, height = device().get_current_resolution()
    UtilTouch.airtest_touch_point(width / 2, height / 2, '', 3)
    UtilTouch.airtest_touch_point(width / 2, height / 2, '', 3)
    UtilTouch.airtest_touch_point(width / 2, height / 2, '', 3)

    # 领取邮件
    keyevent('{ESC}')
    time.sleep(2)

