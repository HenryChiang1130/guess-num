import random
start = input('請決定隨機數字範圍開始值: ')
end = input('請輸入隨機數字範圍結束值: ')
start = int(start)
end = int(end)
r = random.randint(start, end) # . 是(的)的意思, randint = random integer(隨機整數), randint(start, end)
count = 0
while True:
	count += 1 #count = count + 1
	num = input('請猜數字: ')
	num = int(num)
	if num == r:
		print('你猜中了!')
		print('這是你猜的第', count, '次')
		break
	elif num > r:
		print('小一點') 
	elif num < r:
		print('大一點')
	print('這是你猜的第', count, '次')