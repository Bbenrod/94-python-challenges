from spellchecker import SpellChecker

# Correct Spellings

def correction(text):
    spell = SpellChecker()
    words = text.split()
    res = map(lambda word: spell.correction(word), words)
    return " ".join(res)


if __name__ == "__main__":
    text = input("GIVE A PHRASE:\t")
    text_corrected = correction(text)
    print("CORRECTED TEXT:\t", text_corrected)

# # find those words that may be misspelled
# misspelled = spell.unknown(['something', 'is', 'hapenning', 'here'])

# for word in misspelled:
#     # Get the one `most likely` answer
#     print(spell.correction(word))

#     # Get a list of `likely` options
#     print(spell.candidates(word))
