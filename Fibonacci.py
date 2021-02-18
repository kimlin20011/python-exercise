number = int(input('輸入數字：'))

a = 0
b = 1
for i in range(number):
    a, b = b, a + b
    print(a, end=' ')
