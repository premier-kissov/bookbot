def get_num_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    character_count = {}
    lower_string = text.lower()
    for character in lower_string:
        if character in character_count:
            character_count[character] +=1
        else:
            character_count[character] = 1
    return character_count

def sort_on(items):
    return items["num"]

def sorted_list(character_count):
    sorted_list =[]
    for character in character_count:
        temp_dict = {}
        temp_dict["char"] = character
        temp_dict["num"] = character_count[character]
        sorted_list.append(temp_dict)
    sorted_list.sort(reverse=True, key=sort_on)
    return sorted_list