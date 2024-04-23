from typing import Optional, Any

import UtilTouch
from UtilsPaddle import getTextPos


def whereByText(text):
    if '抵制不良游戏' in text and '自律公约' in text:
        print('游戏加载首页')
    elif 'CNRELWin' in text and '输入密码' in text:
        print('登录掉了 需要重新登录')
    elif 'CNRELWin' in text and '点击进入':
        print('等待进入游戏 点击')
        pos1: Optional[Any] = getTextPos('点击进入')
        if pos1:
            cx = (pos1[0][0] + pos1[1][0]) / 2
            cy = (pos1[0][1] + pos1[2][1]) / 2
            UtilTouch.airtest_touch_point(cx, cy, '', 3)
    else:
        print('不知道在什么界面了 当前文字 ' + text)
