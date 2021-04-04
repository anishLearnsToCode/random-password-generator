import random
from src.character_type import CharacterType
from src.characters import DIGITS, LOWERCASE_LETTERS, UPPERCASE_LETTERS, SPECIAL_CHARACTERS, ALL


def get_random_password(*conditions: CharacterType, min_length=8):
    password = ''
    for condition in conditions:
        if condition == CharacterType.DIGIT:
            password += random.choice(DIGITS)
        elif condition == CharacterType.LOWERCASE_LETTER:
            password += random.choice(LOWERCASE_LETTERS)
        elif condition == CharacterType.UPPERCASE_LETTER:
            password += random.choice(UPPERCASE_LETTERS)
        elif condition == CharacterType.SPECIAL_CHARACTER:
            password += random.choice(SPECIAL_CHARACTERS)

    for _ in range(min_length - len(conditions)):
        password += random.choice(ALL)

    return password


print(get_random_password(
    CharacterType.DIGIT,
    CharacterType.DIGIT,
    CharacterType.LOWERCASE_LETTER,
    CharacterType.UPPERCASE_LETTER,
    min_length=10
))
