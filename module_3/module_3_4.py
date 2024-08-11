def single_root_words(root_word, *other_words):
    same_words = []
    for c in other_words:
        if not c.lower().find(root_word.lower()) == -1:
            same_words.append(c)
        if not root_word.lower().find(c.lower()) == -1:
            same_words.append(c)
    return same_words


result1 = single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies')
result2 = single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel')
print(result1)
print(result2)