import os
import re
import string
import random

from graph import Graph, Vertex


def get_words_from_text(text_path):
    with open(text_path, 'r') as f:
        text = f.read()

        # remove [text in here]
        text = re.sub(r'\[(.+)\]', ' ', text)

        # convert all whitespaces to a single space
        text = ' '.join(text.split())
        text = text.lower()  # set all to lower case for comparing
        # remove all punctuation marks
        text = text.translate(str.maketrans('', '', string.punctuation))

    words = text.split()  # split words on spaces
    return words


def make_graph(words):
    g = Graph()

    previous_word = None

    for word in words:
        # add word if not in graph
        word_vertex = g.get_vertex(word)

        # increment word weight by one
        if previous_word:
            previous_word.increment_edge(word_vertex)

        # set word to previous word and iterate
        previous_word = word_vertex

    # generate probability mappings
    g.generate_probability_mappings()

    return g


def compose(g, words, length=50):
    composition = []
    word = g.get_vertex(random.choice(words))  # random word to start
    for _ in range(length):
        composition.append(word.value)
        word = g.get_next_word(word)

    return composition


def main(artist):
    # 1)  get words from text
    # books
    # words = get_words_from_text('texts/hp_sorcerer_stone.txt')

    # song lyrics
    words = []
    for song_file in os.listdir(f'songs/{artist}'):
        if song_file == '.DS_Store':
            continue
        song_words = get_words_from_text(f'songs/{artist}/{song_file}')
        words.extend(song_words)

    # 2) create graph using words
    g = make_graph(words)

    # 3) get the next word for x number (defined by user)

    # 4) display graph
    composition = compose(g, words, 100)
    return ' '.join(composition)


if __name__ == '__main__':
    print(main('drake'))
