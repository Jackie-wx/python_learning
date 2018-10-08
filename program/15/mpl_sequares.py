import matplotlib.pyplot as plt

x_values = list(range(1,1001,10))
y_values = [x**2 for x in x_values]
plt.scatter(x_values,y_values,s=10,cmap=plt.cm.Blues,c=y_values)

# 设置图表标题，并给坐标轴加上标签
plt.title("Square Numbers",fontsize=24)
plt.xlabel("Value",fontsize=14)
plt.ylabel("Square of Value",fontsize=14)

# 设置刻度标记的大小
plt.axis([1,1100,0,1100000])
plt.show()