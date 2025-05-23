def get_book_words(text):
    words = text.split()
    return len(words)

def get_book_count(text):
    words = text.split()
    counts = {}
    for word in words:
        word = word.lower()
        for char in word:
            if char in counts:
                counts[char] += 1
            else:
                counts[char] = 1
    return counts

def sort_on(dict):
    return dict["num"]

def sort_list(counts):
    sorted = []
    for word in counts:
        sorted.append({"char": word, "num": counts[word]})
    sorted.sort(key=sort_on, reverse=True)
    return sorted