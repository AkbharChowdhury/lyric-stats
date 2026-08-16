from collections import Counter, defaultdict
from file_handler import FileHandler


def lyric_stats(path: str):
    lyrics: list[str] = FileHandler.read_file(path).lower().split()
    print(f'{lyrics=}')
    word_mappings: dict[str, set[str]] = defaultdict(set)

    for word in lyrics:
        word_mappings[word[0]].add(word)

    counter = Counter(lyrics)

    return word_mappings, counter



def show_lyrics(word_mappings: dict[str, set[str]]):
    for letter, words in word_mappings.items():
        print(f'{letter}: {" ".join(words)}')