import time

import meituan.meituan as meituan
from pyautogui_demo.meituan.meituan import LEFT_CORNER

if __name__ == '__main__':
    time.sleep(2)
    meituan.move_to(LEFT_CORNER, 2)

    