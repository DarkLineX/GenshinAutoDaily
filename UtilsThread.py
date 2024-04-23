import time


def threadSleep(count, msg):
    for i in range(count):
        print("等待 " + msg + "暂停 " + str(i) + "s中,一共暂停 " + str(count) + "s")
        time.sleep(1)