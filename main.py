def main():
    text = get_book_text("books/frankenstein.txt")
    print(text)

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()