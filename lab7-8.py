def enter_data():

    global total,n
    total = 0
    n = 0
    num = 0
    while num != -1:
        num = int(input(f"Enter value {n+1} : "))
        if (num != -1):
            total += num
            n += 1

#main program
total = 0
n = 0
enter_data()
print(f"Total number : {total}")
print("Average value : ",total//n)
