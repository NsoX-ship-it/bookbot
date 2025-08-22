def get_book_text(filepath):
    
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

print(get_book_text("/home/nathan/boot/bookbot/books/frankenstein.txt"))


    
