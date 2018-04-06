'''question 1: class error emerges in this list'''
'''question 2:  create only one turtle instance because they only refer to one objet'''
''' question 3: same as the picture in 11.11'''
this = ["I", "am", "not", "a", "crook"]
that = ["I", "am", "not", "a", "crook"]
'''print("Test 1: {0}".format(this is that))
that = this
print("Test 2: {0}".format(this is that))'''
'''question 4 :because before the code that = this, that and this refer to different objects in python, whereas after the 
code that=this, they refer to the same object, that's why (this is that) is true'''

#question 5:

def add_vectors(u,v):

    for i in range(len(u)):
        u[i]=u[i]+v[i]

        print(u)

print(add_vectors([1, 1], [1, 1]))
print((add_vectors([1, 2], [1, 4])))
print(add_vectors([1, 2, 1], [1, 4, 3]))

#question 6

def scalar_mult(s,v):
    for i in range(len(v)):
        v[i] = v[i]*s
    return v

print(scalar_mult(5,[1,2]))
print(scalar_mult(3, [1, 0, -1]))

