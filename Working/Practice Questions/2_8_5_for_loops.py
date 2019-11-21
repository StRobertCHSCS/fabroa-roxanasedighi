# initialize total
total = 0

# compute the sum of 10 numbers inputted by the user
for i in range(10):
    user_num = int(input("Enter a number: "))
    total = total + user_num
    
# output total
print("Sum: " + str(total))