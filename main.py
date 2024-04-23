import time
from AutoCore import whereByText, intoGame
from GameProcess import init_win
from UtilsPaddle import getPageText


def login(x, y):
    pass


if __name__ == '__main__':
    win = init_win('')
    while True:
        if whereByText(getPageText()) == 1:
            intoGame()
            break
        else:
            time.sleep(5)

