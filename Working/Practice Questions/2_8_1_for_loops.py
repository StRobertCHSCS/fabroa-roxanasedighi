# get number
number = int(input("Enter a number: "))

# initialize total
total = 0

# compute the total from 1 to number
for i in range(1, number+1):
    # print(i)
    total = total + i

# output total
print(total)
