from collections import Counter


def load_data(filepath):
    f = open(filepath, "r")
    file_content = f.read()
    f.close()
    return file_content


def get_most_frequent_words(text):
    words_list = str.split(text)
    words_to_print = 10
    return Counter(words_list).most_common(words_to_print)


if __name__ == '__main__':
    filename = input()
    file_content = load_data(filename)
    frequent_words = get_most_frequent_words(file_content)
    # Counter.most_common() returns array of pairs (a,b) a - element, b - count, therefore calling word[0] i take
    # element from this pair. its not 'magic number'
    print([word[0] for word in frequent_words])
