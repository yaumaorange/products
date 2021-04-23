import os #載入作業系統模組
	
#讀取檔案
def read_file(filename):
	products = []
	with open(filename, 'r') as f:
		for line in f:
			if '商品,價格' in line:
				continue
			name, price = line.strip().split(',')
			products.append([name, price])
	print(products)
	return(products)

#新增內容
def user_input(products):
	while True:
		name = input('請輸入商品名稱:')
		if name == 'q':
			break
		price = int(input('請輸入價格:'))
		products.append([name, price])
	return(products)
	
def print_products(products):	
	#print(products)
	for p in products:
		print(p[0], '的價格是', p[1])


#寫入檔案
def write_file(filename, products):
	with open(filename, 'w') as f:
		f.write('商品,價格\n')
		for p in products:
			f.write(p[0] + ',' + str(p[1]) + '\n' )


def main():
	filename = input('請輸入檔名:')
	if os.path.isfile(filename): #檢查檔案
		products = read_file(filename)
	else:
		print('沒有這個檔案')

	products = user_input(products)

	print_products(products)

	write_file(filename, products)

main()