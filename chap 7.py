def words_5(words):
    count=0
    for i in words:
        if len(i) ==5:
            count += 1
    return count
words_5(words)