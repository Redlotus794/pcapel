import time

import pyautogui

LEFT_CORNER = (6, 34)
WINDOW_SIZE = (600, 1166)

def move_to(point: tuple, duration=1):
    pyautogui.moveTo(point[0], point[1], duration=duration)


def open_meituan():
    # 520 640
    time.sleep(2)
    pyautogui.click(520, 640)  # 点击美团图标


if __name__ == '__main__':
    open_meituan()