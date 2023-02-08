import numpy as np
from numpy.random import randn

# 產生亂數
def random_number(qq):
	list = []
	i= 0
	while i < qq:
		x = randn()
		list.append(x)
		i += 1
# 計算機率
	in_stdev = 0 # 計算在一個標準差內的次數
	for i in list:
		if i <=1 and i >= -1:
			in_stdev += 1
	result = (in_stdev / len (list))*100 # 在標準差內次數/總數
	print (result, '%')

# main function
random_number (10000000000)
