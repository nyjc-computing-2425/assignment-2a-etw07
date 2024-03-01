num = input('Enter a number (decimal or integer): ')
# type your code here
num2 = num.replace(".","")
num2 = num2.lstrip(" 0")
sf = len(num2)
# do not change any code beyond this point
print('The number', num, 'has', sf, 'significant figures.')
