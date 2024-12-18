headers = "RankStadiumSeating capacityRegionCountryCityImagesHome team(s)"


def extract_uppercase_words(text):
    result = []
    current_word = ""

    for char in text:
        if char.isupper():  # Check if the character starts a new uppercase word
            if current_word:  # If there is an existing word, add it to the result
                result.append(current_word.strip())
            current_word = char  # Start a new word
        else:
            current_word += char  # Append the character to the current word

    if current_word:  # Append the last word if any
        result.append(current_word.strip())

    return result