import matplotlib.pyplot as plt
from random_walk import RandomWalk
while True:
	rw = RandomWalk()
	rw.fill_walk()
	
	# 设置绘图窗口的尺寸
	plt.figure(figsize=(10,6),dpi=720)
	point_numbers = list(range(rw.num_points))
	plt.scatter(rw.x_values,rw.y_values,s=30,c=point_numbers, cmap=plt.cm.Blues)
	
	# 突出起点和终点
	plt.scatter(0,0,c='green',s=50)
	plt.scatter(rw.x_values[-1],rw.y_values[-1],c='red',s=50)
	
	# 隐藏坐标轴
	plt.axes().get_xaxis().set_visible(False)
	plt.axes().get_yaxis().set_visible(False)
	
	plt.show()
	keep_running = input("Make another walk?(y/n): ")
	if keep_running == 'n':
		break