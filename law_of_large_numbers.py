import numpy as np
from numpy.random import randn

# 產生亂數
def random_number(qq):
	number = []
	i= 0
	while i < qq:
		x = randn()
		number.append(x)
		i += 1
	return number

# 計算機率
def posibility(list_name):
	in_stdev = 0 # 計算在一個標準差內的次數
	for i in list_name: 
		if i <=1 and i >= -1:
			in_stdev += 1
	result = (in_stdev / len (list_name))*100 # 在標準差內次數/總數
	print (result, '%')

# 輸入與計算
while True:
	ask = input ('請輸入母體總數：')
	if ask == 'q':
		break
	else:
		s = random_number (int(ask)) # return存取的資料需要宣告變數
		posibility (s)