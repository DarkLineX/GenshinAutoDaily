import logging

from airtest.core.api import snapshot
from paddleocr import PaddleOCR

# 关闭日志
logging.getLogger('ppocr').setLevel(logging.ERROR)
ocr = PaddleOCR(use_angle_cls=True, lang="ch")


def paddleText(img_path):
    # need to run only once to download and load model into memory
    result = ocr.ocr(img_path, cls=True)
    return result


def getPageText():
    test_pic = 'snap_pic.png'
    snapshot(test_pic)
    result_list = paddleText(test_pic)
    ptext = ""
    for r in result_list[0]:
        print(r)
        ptext = ptext + " " + r[1][0]
    return ptext


def getTextPos(text):
    test_pic = 'snap_pic.png'
    snapshot(test_pic)
    result_list = paddleText(test_pic)
    pos = None
    for r in result_list[0]:
        if text == str(r[1][0]).strip():
            pos = r[0]
    return pos


if __name__ == '__main__':
    pass
