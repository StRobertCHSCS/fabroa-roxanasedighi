'''
put header here
'''

# get the exchange
exchange_rate = float(input("Enter the CAD to USD exchange rate: "))

# get the starting and ending value
start_value = int(input("Enter the start value: "))
end_value = int(input("Enter the end value: "))

# print out chart header
print("CAD Price  -->  USD Price")

# output chart
for cad in range(start_value, end_value+1, 10):
    usd = exchange_rate * cad
    print(cad, " --> ", usd) 