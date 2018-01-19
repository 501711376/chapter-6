number = [0,2,3,7,11,12]
count_odd=0
count_even=0
for x in number:
    if not x%2 :
        count_even+=1
    else:
        count_odd+=1
print("Number of odd numbers : ", count_odd)