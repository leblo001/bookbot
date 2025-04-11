from collections import Counter

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
    return file_contents

def get_num_words(passage):
    words = passage.split()
    return len(words)

def get_num_chars(book):
     num_chars = {}
     for c in book:
         c = c.lower()
         if c not in num_chars:
             num_chars[c] = 1
         else:
             num_chars[c] += 1
     return num_chars   

# def get_num_chars(book):
#     count = Counter(book)
#     return count

def sort_dict(dict):
    list_of_tuples = list(dict.items())
    s = sorted(list_of_tuples, key=lambda x: x[1], reverse=True)
    list_of_dict = []
    for char, count in s:
        if char.isalpha():
            d = {'character' : char, "count": count}
            list_of_dict.append(d)
    return list_of_dict
