from collections import Counter


def load_data(filepath):
    f = open(filepath, "r")
    text = f.read()
    f.close()
    return text


def get_most_frequent_words(text):
    split_text = str.split(text)
    words_to_print = 10
    return Counter(split_text).most_common(words_to_print)


if __name__ == '__main__':
    filename = input()
    text = load_data(filename)
    frequent_words = get_most_frequent_words(text)
    # Counter.most_common() returns array of pairs (a,b) a - element, b - count, therefore calling word[0] i take
    # element from this pair. its not 'magic number'
    print([word[0] for word in frequent_words])
