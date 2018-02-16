#question 12
def remove(phrase, word):
    new = word.replace(phrase, "")
    return new


print(remove("apple", "appleee"))

#question 8
def reverse(word):
    new = ""
    for i in range(len(word)):
        new += word[len(word)-i-1]
    return print(new)

def mirror(word):
    return word + reverse(word)


mirror("woo")

#question 9

def remove_letter(letter, word):
    new = ""
    for ch in word:
        if ch != letter:
            new += ch
    return print(new)

remove_letter("o", "bobobo")

#question 3

def count_letters(fruit, letter, start):
    index = start
    while index < len(fruit):
        if fruit[index] == letter:
            print (index)
        index += 1
    return -1


def sum_all_evens(lst):
    even_sum = 0
    for e in lst:
        if e % 2 == 0:
           
            even_sum = even_sum + e

    return even_sum


test_list = [6, 5, 4, 0 , -3]
print(sum_all_evens(test_list))

testEqual(sum_all_evens([4, -2, 3]), 2)
testEqual(sum_all_evens([4, 2, 3]), 6)