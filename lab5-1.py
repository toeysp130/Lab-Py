inp = (input('Enter integer number( 4 digit : )'))
print()
num1 =int(inp[0])
num2 =int(inp[1])
num3 =int(inp[2])
num4 =int(inp[3])
Max = num1
if Max < num2:
    Max = num2
if Max < num3:
    Max = num3
if Max < num4:
    Max = num4
print()
print (f'Maximum Digit of integer number {inp} = {Max}')


