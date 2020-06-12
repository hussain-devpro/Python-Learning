from my_urllib import (fetch_words, print_items)


words = fetch_words('http://www.rapconverter.com/SampleDownload/Sample.txt')
print_items(words)