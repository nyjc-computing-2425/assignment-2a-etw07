num = input('Enter a number (decimal or integer): ')
# type your code here
num2 = num.replace(".","").replace(" ","").lstrip("0")
sf = len(num2)
# do not change any code beyond this point
print('The number', num, 'has', sf, 'significant figures.')
