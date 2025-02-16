def main():
    print("--- Begin report of books/frankenstein.txt ---")

    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        print(f"{get_word_count(file_contents)} words found in the document\n")
        get_repeat_character_count(file_contents)
    
    print("\n--- End report ---")    

def get_word_count(string):
    word_count = 0
    split_string = string.split()
    word_count = len(split_string)
    return word_count

def get_repeat_character_count(string):

    lowered_string = string.lower()
    character_dict = {}
    for c in lowered_string:
        if c in character_dict.keys():
            character_dict[c] = character_dict[c] + 1
        else:
            character_dict[c] = 1
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    for k in character_dict.keys():
        if not k in alphabet:
            continue
        else:
            print(f"The '{k}' character was found {character_dict[k]} times")

    
        

main()
