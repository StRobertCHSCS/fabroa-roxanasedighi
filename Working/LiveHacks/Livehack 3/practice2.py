
# initialize counter
number_days = 0
total_spent = 0
daily_amount = 0

# loop to get user daily amounts and accumulate total
while daily_amount != -1:
    daily_amount = float(input("Enter a daily spent amount (-1 to stop): "))
    total_spent = total_spent + daily_amount
    number_days = number_days + 1

# compute allowable spent 
allowable_spent = number_days * 250

print("Total days travelled: " +str(number_days))
print("Total amount spent: " + str(total_spent))

# determine if a fee is owed
if total_spent > allowable_spent:
    fee = total_spent * 0.13
    print("You owe a fee of $" +str(round(fee,2)))
else:
    print("Phew, you do not owe a fee")
