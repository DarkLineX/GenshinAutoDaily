import logging

from paddleocr import PaddleOCR

# 关闭日志
logging.getLogger('ppocr').setLevel(logging.ERROR)
ocr = PaddleOCR(use_angle_cls=True, lang="ch")


def paddleText(img_path):
    # 页面文字识别
    # need to run only once to download and load model into memory
    result = ocr.ocr(img_path, cls=True)
    return result


if __name__ == '__main__':
    pass
