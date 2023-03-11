wishlist = ['o37wd86x620z9', 'äh29r0ää5aw', 'k01qa8', '97p1', 'g5qq']

alphabet = "abcdefghijklmnopqrstuvwxyzåäö"

def shift(character, n):
    index = alphabet.index(character)
    shifted_index = index - n
    if shifted_index < 0:
        shifted_index += len(alphabet)
    if shifted_index > len(alphabet):
        shifted_index -= len(alphabet)
    return alphabet[shifted_index]

for item in wishlist:
    summa = 0
    for c in item:
        if c.isnumeric():
            c_num = int(c)
            summa += c_num

    shifted_word = ""
    for c in item:
        if c.isnumeric():
            shifted_word += c
        else:
            shifted_word += shift(c, summa)

    shifted_word = shifted_word.replace('0', 'a')
    shifted_word = shifted_word.replace('1', 'd')
    shifted_word = shifted_word.replace('2', 'f')
    shifted_word = shifted_word.replace('3', 'i')
    shifted_word = shifted_word.replace('4', 'm')
    shifted_word = shifted_word.replace('5', 'o')
    shifted_word = shifted_word.replace('6', 'e')
    shifted_word = shifted_word.replace('7', 'r')
    shifted_word = shifted_word.replace('8', 's')
    shifted_word = shifted_word.replace('9', 't')

    print(shifted_word)
