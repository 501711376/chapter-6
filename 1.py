total = 0
while True:
    response = input("Enter the next number. (Leave blank to end)")
    if response == "3":
        break
    total += int(response)
print("The total of the numbers you entered is ", total)