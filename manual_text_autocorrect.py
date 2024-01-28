from autocorrect import Speller
import enchant

diction = enchant.Dict("en_US")

weird_texts = [
    "               cat",
    "ccat",
    "cccccccccccat",
    "caaaaaaaat",
    "catttttttt",
    "      catttttt",
    "       ccccccaaaaaaattttttt       ",
    "caat",
    "catd",
    "dcat",
    "hcat",
    "cddat",
    "hi        cat",
    "chat",
    "c     at",
    "my c at is cute",
    " i m y c at"
]

def fix_text(text):
    # remove leading and trailing spaces
    text = text.strip()

    # remove repeated characters
    for letter in text:
        repeated_sequence = letter * 3
        while repeated_sequence in text:
            text = text.replace(repeated_sequence, letter)

    # run autocorrect
    spell = Speller()
    text = spell(text)

    # fix broken words
    split_text = text.split()
    for i in range(len(split_text) - 1):
        try_combination = split_text[i] + split_text[i + 1]
        if len(split_text[i]) > 0 and len(split_text[i + 1]) > 0 and diction.check(try_combination):
            split_text[i] = try_combination
            split_text[i + 1] = ""

    text = " ".join(split_text)

      # remove extra spaces
    text = " ".join(text.split())


    return text

for text in weird_texts:
    print(fix_text(text))