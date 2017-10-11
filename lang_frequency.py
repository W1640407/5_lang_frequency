from collections import Counter


def load_data(filepath):
    f = open(filepath, "r")
    text = f.read()
    f.close()
    return text


def get_most_frequent_words(text):
    split = str.split(text)
    c = Counter(split).most_common(10)
    return c


if __name__ == '__main__':
    text = load_data('test.txt')
    frequent_words = get_most_frequent_words(text)
    print([i[0] for i in frequent_words])
