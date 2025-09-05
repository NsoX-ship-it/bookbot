from stats import book_character_count
from stats import book_word_count 

def main():
    book_filepath = "/home/nathan/boot/bookbot/books/frankenstein.txt"
    book_text = get_book_text(book_filepath)
    word_count = book_word_count(book_text)
    print(f"{word_count} words found in the document")
    character_count = book_character_count(book_text)
    print(character_count)

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents
 
main()










    
