#!/usr/bin/env python3
from bs4 import BeautifulSoup

with open('directory.html') as f:
    text = f.read()

soup = BeautifulSoup(text, 'html.parser')

people = soup.find_all('td', {'class': 'person'})

with open('researchers.txt', 'w') as f:
    for person in people:
        name = person.find('a').text
        f.write(name + '\n')
