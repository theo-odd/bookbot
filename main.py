def word_count(text):
    words = text.split()
    return len(words)

def get_text(book_path):
    with open(book_path) as f:
        return f.read()
    
def count_instances(text):
    g_text = text.lower()
    d = {}
    for letter in g_text:
        if letter in d:
            d[letter] += 1
        else:
            d[letter] = 1
    return d

def main():
    book_path = "books/frankenstein.txt"
    text = get_text(book_path)
    num_word = word_count(text)
    instances = count_instances(text)
    print(f"--- Begin report of {book_path} ---")
    print(f"there are {num_word} words in this text !\n")
    for i in instances:
        if ord(i) >= 97 and ord(i) <= 122:
            print(f"The {i} character was found {instances[i]} times")
    print("--- End report ---")

main()