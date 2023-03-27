def count_words(text):
    """
    Returns a dictionary of the word lengths in the given text.
    """
    # Clean the text from non-letter characters using a generator expression
    clean_text = ''.join(c for c in text if c.isalpha() or c.isspace())

    # Use dictionary comprehension to count the occurrences of each word
    word_lengths = {word: len(word) for word in clean_text.lower().split()}
    return word_lengths


if __name__ == '__main__':
    text = """
    You see, wire telegraph is a kind of a very, very long cat.
    You pull his tail in New York and his head is meowing in Los Angeles.
    Do you understand this?
    And radio operates exactly the same way: you send signals here, they receive them there.
    The only difference is that there is no cat.
    """
    print(count_words(text))
