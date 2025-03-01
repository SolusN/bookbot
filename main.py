from stats import *
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("========== BOOKBOT ==========")
    print(f"Analyzing book found at {sys.argv[1]}...")

    with open(sys.argv[1]) as f:
        file_contents = f.read()
        print("---------- Word Count ----------")
        print(f"Found {get_word_count(file_contents)} total words")
        print("---------- Character Count ----------")
        get_repeat_character_count(file_contents)

    print("========== End report ==========")    

main()
