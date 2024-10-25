
def frankenstein_content(): 
    frankenstein_path = 'books/frankenstein.txt'

    with open(frankenstein_path) as f:
        file_contents = f.read()
        #print(file_contents)
    return file_contents


def count_words(file_contents): 
    words = file_contents.split()
    count = 0 
    for word in words:
        count += 1 
    return count

def character_count(): 
    file_content = frankenstein_content()
    words = file_content.split()
    character_count = {}

    for word in words:
        word = word.lower()
        for char in word:
            if char in character_count:
                character_count[char] += 1
            else:
                character_count[char] = 1
    return character_count


def create_character_list():
    character_dict = character_count()
    #converting dictionary value to a list
    char_list = []
    for character in character_dict:
        tmp_dict = {}
        count = character_dict[character]
        tmp_dict['character'] = character
        tmp_dict['count'] = count
        char_list.append(tmp_dict)
    char_list.sort(reverse=True, key = lambda x: x['count'])
    return char_list



character_list = create_character_list()

print(character_list)

file_content = frankenstein_content()
count = count_words(file_content)

print("--- Begin report of books/frankenstein.txt ---")
print(f"{count} words found in the document")

for item in character_list:
    character = item['character']
    count = item['count']
    if character.isalpha():
        print(f"The '{character}' was found {count} times")
print("--- End report ---")
