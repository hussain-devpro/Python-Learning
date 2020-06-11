from my_urllib import (fetchWords, print_items)


words = fetchWords('http://www.rapconverter.com/SampleDownload/Sample.txt')
print_items(words)