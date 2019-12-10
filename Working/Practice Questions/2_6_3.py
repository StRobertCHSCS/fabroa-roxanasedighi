number = int(input("Enter a number: "))

i = 0
while 2**i <= number:
    i += 1

print("exponent:", i-1)
print("2**n:", 2**(i-1))