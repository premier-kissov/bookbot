import sys
from stats import get_num_words, count_characters,sorted_list

def main():
    path_to_file = sys.argv[1]
    text = create_string(path_to_file)
    words = get_num_words(text)
    character_count = count_characters(text)
    sorted = sorted_list(character_count)
    print("============ BOOKBOT ============")
    print(f"Analysing book found at {path_to_file}...")
    print("----------- Word Count ----------")
    print(f"Found {words} total words")
    print("-------- Character Count --------")
    for character in sorted:
        print(f"{character["char"]}:" + " " +f"{character["num"]}")
    
def create_string(path_to_file):
    with open(path_to_file) as f:
        book_string = f.read()
    return book_string

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    main()

