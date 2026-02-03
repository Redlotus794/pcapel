import pyautogui
import time

# 暂停2秒，给你切换到目标窗口的时间
time.sleep(2)
pyautogui.PAUSE = 1 # 每个PyAutoGUI调用后暂停1秒

pyautogui.moveTo(50, 120, duration=3)
pyautogui.click()
pyautogui.typewrite("Hello, PyAutoGUI! \n")


# # 移动鼠标到屏幕坐标(100, 200)，耗时1秒（平滑移动）
# pyautogui.moveTo(672, 10699, duration=1)
# # 模拟鼠标左键单击
# pyautogui.click()
#
# # 模拟键盘输入文字
# pyautogui.typewrite("Hello, PyAutoGUI! \n")
#
# # 模拟按下并释放组合键 Ctrl+S
# # pyautogui.hotkey('ctrl', 's')
# # pyautogui.
#
# pyautogui.moveTo(672, 6000, duration=3)
# pyautogui.click()
# pyautogui.scroll(10)
# pyautogui.scroll(-10)
#
# # 获取屏幕尺寸
# screen_width, screen_height = pyautogui.size()
# print(f"屏幕分辨率：{screen_width}x{screen_height}")
#
# screenshot = pyautogui.screenshot()
# screenshot.save('screenshot.png')