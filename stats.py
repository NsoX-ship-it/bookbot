def book_word_count(book_text):
    book_words = book_text.split()
    book_word_count = len(book_words)
    return book_word_count

def book_character_count(book_text):
    character_count = {}
    book_words = book_text.lower()
    book_characters = list(book_words) 
    for characters in book_characters:
        if characters in character_count:
            character_count[characters] += 1
        else:
            character_count[characters] = 1
    return character_count
    