def word_counter(words):
    word_array = words.split(' ')
    word_count = len(word_array)
    return word_count

def get_character_counts(book_text):
    character_counts = {}
    book_lowered = book_text.lower()
    for i in range(0, len(book_lowered)-1):
        character = book_lowered[i]
        if character not in character_counts:
            character_counts[character] = 0
        character_counts[character] += 1
    return character_counts

def sort_dict(dict):
    temp_list = []
    sorted_dict = {}
    for key, value in dict.items():
        temp_list.append(key)
    temp_list.sort(reverse=False)
    for item in temp_list:
        if item.isalpha():
            sorted_dict[item]=dict[item]
    return sorted_dict
