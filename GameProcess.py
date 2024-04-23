import logging
import os
import signal
import subprocess
import psutil
from airtest.cli.parser import cli_setup
from airtest.core.api import auto_setup, device

from UtilsThread import threadSleep

logger = logging.getLogger("Genshin")
process_name = "YuanShen"


def re_start_app(msg):
    try:
        logger.error('杀死原神进程...' + '原因' + msg)
        killGame()
        threadSleep(5, '杀死原神进程等待启动')
        logger.error('启动原神进程...')
        lunchGame()
        threadSleep(10, '启动原神等待启动完成')
    except Exception as e:
        logger.error("异常启动" + str(e))


def killGame():
    pid = get_app_pid()
    if pid > 0:
        os.kill(pid, signal.SIGTERM)
    else:
        logger.error('未找到原神进程 无法杀死进程')


def get_app_pid():
    for proc in psutil.process_iter():
        try:
            process = psutil.Process(proc.pid)
            name = process.name()
            if process_name in name:
                return proc.pid
        except (psutil.NoSuchProcess, psutil.AccessDenied, psutil.ZombieProcess):
            pass
    return 0


def lunchGame():
    gen_proc = subprocess.Popen('D:\game\Genshin Impact Game\YuanShen.exe')
    if gen_proc:
        logger.error('启动成功')
        return True
    else:
        logger.error('启动失败')
        return False


def init_airtest():
    try:
        if not cli_setup():
            auto_setup(__file__, logdir=False, devices=["Windows:///?title_re=.*原神*", ])
        logger.info("start...")
        d = device()
        return d
    except Exception as e:
        logger.error('启动异常，无法找到原神游戏窗口' + str(e))
        return None


def init_win(msg):
    re_start_app(msg)
    return init_airtest()