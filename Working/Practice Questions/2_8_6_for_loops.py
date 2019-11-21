# intialize the total
total = 0

# get the number of numbers from user
num_num = int(input("How many numbers do you want to total: "))

# compute the total
for i in range(num_num):
    user_num = int(input("Enter a number: "))
    total = total + user_num

# output total
print("Sum: " + str(total))