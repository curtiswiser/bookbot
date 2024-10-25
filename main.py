frankenstein_path = 'books/frankenstein.txt'

with open(frankenstein_path) as f:
    file_contents = f.read()
    print(file_contents)