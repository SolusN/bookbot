
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
	
	
	sorted_character_dict = dict(sorted(character_dict.items(), key=lambda item: item[1], reverse=True))


	for k in sorted_character_dict.keys():
		if not k in alphabet:
			continue
		else:
			print(f"{k}: {character_dict[k]}")
