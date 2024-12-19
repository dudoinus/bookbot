def word_count(text):
    return len(text.split())

def character_count(text):
    lowered_string = text.lower()
    num_of_chars = {}
    for char in lowered_string:
        if char in num_of_chars and char.isalpha():
            num_of_chars[char] += 1
        elif char not in num_of_chars and char.isalpha():
            num_of_chars[char] = 1
    return num_of_chars

def sort_on(dict):
    return dict["num"]

def main():
    with open("github.com/dudoinus/bookbot/books/frankenstein.txt") as f:
        file_contents = f.read()
        word_total = word_count(file_contents)
        chars = character_count(file_contents)
        chars_list = []
        for char, count in chars.items():
            chars_list.append({"char": char, "num": count})
        chars_list.sort(reverse=True, key=sort_on)
    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_total} words found in the document\n")
    for char_dict in chars_list:
        print(f"The '{char_dict['char']}' character was found {char_dict['num']} times")
    print("--- End report ---")
main()