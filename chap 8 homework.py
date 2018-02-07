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