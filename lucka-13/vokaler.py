vowels_count = 0
consonants_count = 0
vowels = ['a', 'e', 'i', 'o', 'u', 'y', 'å', 'ä', 'ö', 'n', 'v']
consonants = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'l', 'm', 'p', 'q', 'r', 's', 't', 'w', 'x', 'z']
poem = "Midvinternattens köld är hård, stjärnorna gnistra och glimma. Alla sova i enslig gård djupt under midnattstimma. Månen vandrar sin tysta ban, snön lyser vit på fur och gran, snön lyser vit på taken. Endast tomten är vaken."

for p in poem:
    if p in vowels:
        vowels_count += 1
    elif p in consonants:
        consonants_count += 1

result = vowels_count - consonants_count

if 5 >= result >= -5:
    print("Yes!")
else:
    print("No!")
