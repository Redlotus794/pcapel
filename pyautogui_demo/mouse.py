import pyautogui

# 开启实时坐标显示（按Ctrl+C终止）
print("鼠标移动到目标位置，终端会显示坐标；按Ctrl+C退出")
try:
    while True:
        # 获取鼠标当前坐标
        x, y = pyautogui.position()
        # 格式化输出，保持一行刷新
        position_str = f"X: {x} Y: {y}"
        print(position_str, end='\r')
except KeyboardInterrupt:
    # 按Ctrl+C时换行并提示结束
    print("\n坐标查看已终止")