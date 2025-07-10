
from stats import get_book_text, count_characters

def main():
    text = get_book_text()
    num_words = len(text.split())
    print(f"{num_words} words found in the document.")
    char_counts = count_characters(text)
    print(char_counts)

if __name__ == "__main__":
    main()
