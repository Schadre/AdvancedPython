a_text = 'In computing, a hash table hash map is a data structure which implements an associative array abstract data type, a structure that can map keys to values. A hash table uses a hash function to compute an index into an array of buckets or slots from which the desired value can be found'


def word_count(sentence):
    sentence = sentence.lower()
    dictionary = {}
    a_text = sentence.split()
    for num_word in a_text:
        count = 0
        for word in a_text:
            if num_word == word:
                count += 1
        dictionary[num_word] = count
    return dictionary

print(word_count(sentence= a_text))

