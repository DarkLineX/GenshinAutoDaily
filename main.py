import time

from airtest.core.api import snapshot

import UtilsImage
from AutoCore import whereByText, intoGame
from GameProcess import init_win
from UtilsPaddle import getPageText


def login(x, y):
    pass


if __name__ == '__main__':
    win = init_win('')
    while True:
        if whereByText(getPageText()) == 1:
            time.sleep(5)
            intoGame()
            break
        else:
            time.sleep(5)

