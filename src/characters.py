DIGITS = tuple(str(x) for x in range(10))
LOWERCASE_LETTERS = tuple(chr(ord('a') + x) for x in range(26))
UPPERCASE_LETTERS = tuple(map(str.upper, LOWERCASE_LETTERS))
SPECIAL_CHARACTERS = ('@', '#', '$', '%', '=', ':', '?', '.', '/', '|', '~', '>', '*', '(', ')', '<')
ALL = DIGITS + LOWERCASE_LETTERS + UPPERCASE_LETTERS + SPECIAL_CHARACTERS
