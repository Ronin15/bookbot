
from stats import get_book_text, count_characters, sort_character_count

def main():
    text = get_book_text()
    num_words = len(text.split())
    char_counts = count_characters(text)
    sorted_chars = sort_character_count(char_counts)
    
    print("================ BOOKBOT========================\n")
    print("Analyzing book found at books/frankenstein.txt.\n")
    print(f"--------------- Word count ---------------------\n")
    print(f"Found {num_words} total words\n")
    print("--------------- Character count -----------------\n")
    for char_data in sorted_chars:
        print(f"{char_data['char']}: {char_data['num']}\n")
    
    print("================= END =========================\n")

if __name__ == "__main__":
    main()
