# 看看没有读取第一行会怎么样
import csv

filename = 'sitka_weather_07-2014.csv'
with open(filename) as f:
	reader = csv.reader(f)
	highs = []
	head_row = next(reader)  ### 读取第一行之后，后面的循环会从第二行，也就是数据那一行开始读取
	for row in reader:
		highs.append(row[1])
	print(highs)