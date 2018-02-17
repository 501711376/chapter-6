#question 12
def remove(phrase, word):
    ab = word.replace(phrase, "")
    return ab


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

def count_letters(fruit,count):
    fruit = "banana"
    count = 0
    for char in fruit:
        if char == "a":
            count += 1
    print(count)

#question 4
def count_letters(strng,ch,start=0):
    ix = start
    while ix < len(strng):
        if strng[ix] == ch:
            return ix
        ix += 1
    return -1

print(count_letters("banana", "a", 2) == 3)


