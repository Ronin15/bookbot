def get_book_text():
    with open("books/frankenstein.txt") as f:
        # Read the entire content of the file
        return f.read()

def main():
    text = get_book_text()
    print(text)

if __name__ == "__main__":
    main()
