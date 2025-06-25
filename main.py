import sys
from stats import get_num_words, get_num_chars, sorted_list
def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
    text = get_book_text(sys.argv[1])
    num_words = get_num_words(text)
    num_char = get_num_chars(text)
    list = sorted_list(num_char)
    print("============ BOOKBOT ============")
    print(f"Analyzing Book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in list:
        char = item["char"]
        num = item["num"]
        if char.isalpha():
            print(f"{char}: {num}")
    print("============= END ===============")            

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()