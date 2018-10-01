'''
Grabs DOI's from Google Scholar ID's
'''
import requests
import pandas as pd
from bs4 import BeautifulSoup

def get_titles(author_id):
    url = "https://scholar.google.com/citations?user={}"
    r = requests.get(url.format(author_id))
    soup = BeautifulSoup(r.text, 'html.parser')
    links = soup.find_all('a', {'class': 'gsc_a_at'})
    return [links[i].text for i in range(len(links))]

def write_author(author, author_id, file_):
    titles = get_titles(author_id)
    if titles: 
        for title in titles:
           file_.write(author + '\t' + title + '\n')

df = pd.read_csv('uchicago.csv', names=['author', 'id', 'mail'])

with open('author_title_file.txt', 'w') as f:
    for index_, (author, id, mail) in df.iterrows():
        write_author(author, id, f)
        print(author)
