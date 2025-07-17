from stats import word_count, character_counts, list_dict
import sys

# ./books/frankenstein.txt
# ./books/mobydick.txt
# ./books/prideandprejudice.txt

def get_book_text(path):
    with open(path) as f:
        file_contents = f.read()
    return file_contents

def print_report(path, count, l_counts):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path}...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for l in l_counts:
        if l["char"].isalpha():
            print(f"{l["char"]}: {l["num"]}")
    print("============= END ===============")

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    book_text = (get_book_text(path))
    count = word_count(book_text)
    c_counts = character_counts(book_text)
    l_counts = list_dict(c_counts)
    print_report(path, count, l_counts)


main() 