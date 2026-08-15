from collections import Counter, defaultdict
from file_handler import FileHandler


def lyric_stats(path: str):
    data = FileHandler.read_file(path)
    lyrics = data.lower().split()

    word_mapping: dict[str, set[str]] = defaultdict(set)

    for word in lyrics:
        word_mapping[word[0]].add(word)

    counter = Counter(lyrics)

    return word_mapping, counter



def show_lyrics(word_mappings: dict[str, set[str]]):
    for letter, words in word_mappings.items():
        print(f'{letter}: {" ".join(words)}')