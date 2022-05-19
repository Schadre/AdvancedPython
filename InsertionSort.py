def insertion_sort(words):
    # loop over all the elements in the list starting at 1
    for i in range(1, len(words)):
        word = words[i]
        # move elements of list [0 .. i-1], that are
        # greater than words, to one position ahead
        # of the current position
        j = i -1
        while j >= 0 and word < words[j]:
            words[j+1] = words[j]
            j -= 1
            words[j+1] = word
    return words

words = ['this' , 'is', 'a', 'sentence', '.']
print(f"Original string: {words}")
sorted_words = insertion_sort(words)
print(f"Sorted: {sorted_words}")