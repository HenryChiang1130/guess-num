import random
r = random.randint(1, 100) # . 是(的)的意思, randint = random integer(隨機整數), randint(start, end)
while True:
	num = input('請猜數字: ')
	num = int(num)
	if num == r:
		print('你猜中了!')
		break
	elif num > r:
		print('比答案大') 
	elif num < r:
		print('比答案小')