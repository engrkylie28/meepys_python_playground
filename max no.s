num = int(input("Type in a number"))
num1 = int(input("Type in a number"))
num2 = int(input("Type in a number"))
num3 = int(input("Type in a number"))
num4 = int(input("Type in a number"))


num_list = []
num_list.append(num)
num_list.append(num1)
num_list.append(num2)
num_list.append(num3)
num_list.append(num4)

num_list = [num, num1, num2, num3, num4]
largestnum = []
for num in num_list:
    if largestnum < num: # Dont wok.. sob
        largestnum = num
    print(f"{largestnum} is the largest number in {num_list}")
