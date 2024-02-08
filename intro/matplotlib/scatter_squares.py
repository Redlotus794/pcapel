import matplotlib.pyplot as plt
# plt.scatter(2, 4)
# plt.show()

# x_values = [1,2,3,4,5]
# y_values = [1,4,9,16,25]
# plt.scatter(x_values, y_values, s=100) 
# 设置图表标题并给坐标轴加上标签

x_values = list(range(1,1001))
y_values = [x**2 for x in x_values]
plt.scatter(x_values, y_values, c=y_values, cmap=plt.cm.Blues, edgecolor='none', s=40)

plt.axis([0, 1100, 0, 1100000])
plt.show()