# get number
start = int(input("Enter your starting number: "))
end = int(input("Enter your ending number: "))

# output appropriate range
if start < end:
    for i in range(start, end+1):
        print(i)
else:
    for i in range(start, end-1, -1):
        print(i)