from stats import get_book_words, get_book_count, sort_list
import sys

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    
    path = sys.argv[1]
    text = get_book_text(path)
    num_words = get_book_words(text)
    counts = get_book_count(text)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    sorted = sort_list(counts)
    for entry in sorted:
        if(entry["char"].isalpha()):
            print(f"{entry["char"]}: {entry["num"]}")


main()