def find(strng, ch, start=0):
    ix = start
    while ix < len(strng):
        if strng[ix] == ch:
            return ix

        ix += 1
    return -1

find("banana", "a")