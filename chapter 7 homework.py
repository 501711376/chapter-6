#question 1
list=[-1,-3,1,2,3,4,5,6,7,8,9,10]

def count_odd(list):
    count=0
    for i in list:
        if i % 2 == 1:
            count+=1
    return count
print(count_odd(list))

#question 2

def sum_even(list):
    count = 0
    for i in list:
        if i%2 == 0:
            count+=i
    return count
print(sum_even(list))

#question 3

def sum_neg(list):
    count=0
    for i in list:
        if i < 0:
            count += i
    return count
print(sum_neg(list))

#question 4
wordslist= ["asjsad","sajsa","duwisa","dsjks","sdjksdssds"]
def count_words(wordslist):
    count=0
    for i in wordslist:
        if len(i)==5:
            count+=1
    return count
print(count_words(wordslist))

#question 5
def sum_notinclude_firsteven(list):
    count=0
    for i in list:
        if i%2==0:
            break
        count+=i
    return count
print(sum_notinclude_firsteven(list))
#6

samlist=["apple","orange","banana","papa","sam","berry"]
def include_Sam(samlist):
    count=0
    for i in samlist:
        if i == "sam":
            count+=1
            break
        count+=1
    return count
print(include_Sam(samlist))

#7
def sqrt(n):
    approx = n/2.0    
    while True:
        better = (approx + n/approx)/2.0
        print(better)
        if abs(approx - better) < 0.001:
            return better
        approx = better
print(sqrt(25.0))
    
#10
def is_prime(n):              
    for i in range(2,n):
        if n % i == 0:
            return False
        return True
print(is_prime(9))
print(is_prime(8))

#11

import turtle
wn = turtle.Screen()
drunken = turtle.Turtle()
data=[(160, 20), (-43, 10), (270, 8), (-43, 12)]
for [angle,steps] in data:
    drunken.left(angle)
    drunken.forward(steps)
#12

import turtle
wn = turtle.Screen()
drunken = turtle.Turtle()
drunken.pensize(12)

data=[(90,100),(270,100),(120,100),(120,100),(75,142),(135,100),(135,142),(135,100)]

for [angle, steps] in data:
    drunken.left(angle)
    drunken.forward(steps)






        



        