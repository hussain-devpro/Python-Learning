"""
Retrieve and print list of words from URL.

Usage:
    python3 my_urllib.py <url>
"""
import sys
from urllib.request import urlopen


def fetch_words(url):
    """Fetch list of words from URL"""
    story = urlopen(url)
    story_words = []
    for line in story:
        line_words = line.decode('utf8').split()
        for word in line_words:
            story_words.append(word)
    story.close()
    return story_words


def print_items(items):
    print(items)


def main(url):
    words = fetch_words(url)
    print_items(words)


if __name__ == '__main__':
    main(sys.argv[1])  # The 0th arg is the module filename
