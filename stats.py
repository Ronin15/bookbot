def get_book_text(path):
    with open(path) as f:
        # Read the entire content of the file
        return f.read()

def count_characters(text):
    char_counts = {}
    for char in text.lower():
        if char.isalpha():
            if char in char_counts:
                char_counts[char] += 1
            else:
                char_counts[char] = 1
    return char_counts

def sort_character_count(char_counts):
    sorted_chars = []
    for char, count in char_counts.items():
        sorted_chars.append({"char": char, "num": count})
    sorted_chars.sort(key=lambda x: x["num"], reverse=True)
    return sorted_chars
