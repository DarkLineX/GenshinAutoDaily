import logging
import subprocess

logger = logging.getLogger("Genshin")


# 检测


# 退出


def openGame():
    gen_proc = subprocess.Popen('D:\game\Genshin Impact Game\YuanShen.exe')
    if gen_proc:
        logger.error('启动成功')
        return True
    else:
        logger.error('启动失败')
        return False


if __name__ == '__main__':
    if openGame():
        pass

