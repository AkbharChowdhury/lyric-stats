from pathlib import Path

from lyric_stats import lyric_stats, show_lyrics
from song import Song


def show_results(results: dict[str, str]) -> None:
    for name, result in results.items():
        print(name.title())
        show_border()
        print(result)


songs: dict[str, str] = {
    'rockabye': 'lyrics/rockabye.txt',
    'ciao-adios': 'lyrics/ciao-adios.txt',
}
rockabye, ciao_adios = songs.values()


def show_border(n: int = 60) -> None:
    print('-' * n)


def find_keywords(song: Song, keywords: list[str]) -> str:
    return song.find_keyword_occurrences(keywords)


def show_lyrics_details(name_of_lyrics: str) -> None:
    song_name = Path(name_of_lyrics).stem
    print(f'Lyrics stats: {song_name.title()}')
    show_border(n=50)
    word_mappings, counter = lyric_stats(name_of_lyrics)
    show_lyrics(word_mappings)
    print(counter)


def main():
    rockabye_keywords: list[str] = [
        'rockabye',
        'love',
        'She',
        "I'm gonna give you all of my love",
        "I'm gonna rock you"
    ]

    ciao_adios_keywords: list[str] = [
        "I'm not your number one"
    ]

    results: dict[str, str] = {
        'rockabye': find_keywords(Song(rockabye), rockabye_keywords),
        'ciao-adios': find_keywords(Song(ciao_adios), ciao_adios_keywords),
    }
    show_results(results)
    # show_lyrics_details(ciao_adios)


if __name__ == '__main__':
    main()
