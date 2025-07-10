def get_book_text():
    with open("books/frankenstein.txt") as f:
        # Read the entire content of the file
        return f.read()

def count_characters(text):
    char_counts = {}
    for char in text.lower():
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts
