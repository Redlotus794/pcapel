import matplotlib
import matplotlib.pyplot as plt
input_values = [1,2,3,4,5]
squares = [1,4,9,16,25]

matplotlib.use('MacOSX')
plt.plot(input_values, squares, linewidth=5)
plt.title("Square Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Square of Value", fontsize=14)
# 设置刻度标记大小
plt.tick_params(axis='both', labelsize=10)
plt.show()

