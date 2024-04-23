import time
from AutoCore import whereByText
from GameProcess import init_win
from UtilsPaddle import getPageText


def login(x, y):
    pass


if __name__ == '__main__':
    win = init_win('')
    while True:
        whereByText(getPageText())
        time.sleep(5)
