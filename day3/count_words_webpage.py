import requests
import sys

def count_words(url):
    try:
        r = requests.get(url)
    except requests.exceptions.ConnectionError, e:
        print 'Unable to connect to {}: {}'.format(url, e)
    else:
        count = len(r.text.split())
        print '{} has {} words'.format(url, count)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print 'Usage: {} <url> [url]...'.format(sys.argv[0])
        sys.exit(1)

    for url in sys.argv[1:]:
        count_words(url)
