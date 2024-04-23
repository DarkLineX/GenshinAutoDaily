import logging
import time

from airtest.core.api import touch, wait


def airtest_wait_template(template, tag, timeout, sleep=0):
    try:
        logging.info('等待' + str(timeout) + '')
        pos = wait(template, timeout=timeout)
        if pos:
            logging.error('发现点击 进入游戏 图片' + str(pos))
            return pos
    except Exception as e:
        logging.error('未发现 进入游戏 图片' + str(e))
    return None


def airtest_touch_template(template, tag='', sleep=0):
    try:
        pos = touch(template)  # 确认
        if sleep > 0:
            time.sleep(sleep)
        logging.error('点击图片' + ' 点击原因' + tag)
        return pos
    except Exception as e:
        logging.error('点击图片' + ' 点击原因' + tag + '异常' + str(e))
        return None


def airtest_touch_point(x, y, tag, sleep=0):
    try:
        touch((x, y))  # 确认
        if sleep > 0:
            time.sleep(sleep)
        logging.error('点击坐标 x =' + str(x) + ' y = ' + str(y) + ' 点击原因' + tag)
        return True
    except Exception as e:
        logging.error('点击坐标 x =' + str(x) + ' y = ' + str(y) + ' 点击原因' + tag + '异常' + str(e))
        return False
