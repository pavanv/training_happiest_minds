#!/usr/bin/env python

import requests
import sys
from bs4 import BeautifulSoup

def num_links(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text)
    return len(soup.find_all('a'))

if __name__ == '__main__':
    for url in sys.argv[1:]:
        print 'url {} has {} links'.format(url, num_links(url))