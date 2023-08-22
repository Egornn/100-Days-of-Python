from pandas import DataFrame, read_csv

alphabet = read_csv('nato_phonetic_alphabet.csv', encoding='utf-8')
word_to_decode = input('Enter a word you need to spell out: ').upper()
nato_spelling = [{row.letter: row.code for (index, row) in alphabet.iterrows()}[letter] for letter in
                 word_to_decode]
print(nato_spelling)
