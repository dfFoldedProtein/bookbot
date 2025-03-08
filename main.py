from stats import word_counter, get_character_counts, sort_dict
import sys

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def report_print(book_path, total_words, sorted_characters):
    print("========== BOOKBOT ==========")
    print(f"Analyzing book found at {book_path}")
    print("--------- Word Count --------")
    print(f"Found {total_words} total words")
    print("------ Character Count ------")
    for character, count in sorted_characters.items():
        print(f"{character}: {count}")
    print("============ END ============")

def main():
    try:
        desired_text = sys.argv[1]
    except:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    text = get_book_text(desired_text)
    word_count = word_counter(text)
    # find character counts
    character_dicts = (get_character_counts(text))
    # get sorted dictionary
    sorted_dict = (sort_dict(character_dicts))
    report_print(desired_text, word_count, sorted_dict)

main()
