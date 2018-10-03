#!/usr/bin/env python
'''
Grabs DOI's from author and title of an article. 
'''
import csv
import requests
import pandas as pd
from fuzzywuzzy import fuzz
from operator import itemgetter
from urllib.parse import quote as uquote

def possible_doi(author, title, n=10):
    '''
    Takes in an author and title,
    returns a doi, and the best leven dist.
    '''
    url = "https://api.crossref.org/works?rows={}&query.author={}&query.title={}"
    r = requests.get(url.format(n, uquote(author), uquote(title))) 
    print(r, title) 
    d = r.json() 
    doi_list = [] # List of tuples 
    for item in d['message']['items']:
        doi_title = item['title']
        print(doi_title) 
        doi = item['DOI']
        ratio = fuzz.ratio(doi_title, title)  
        doi_list.append((doi_title, doi, ratio)) 

    return max(doi_list, key=itemgetter(2))[1:]

def make_row(author, title):
    '''
    Takes in an author and title,
    returns a dict of author, title, doi, and leven dist.
    '''
    rv = {'author': author, 'title': title}
    rv['doi'], rv['LD'] = possible_doi(author, title)
    return rv

if __name__ == "__main__":
    with open('with_dois.csv', 'w') as csvfile:
        fieldnames = ['author', 'title', 'doi', 'LD']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        with open('author_title_file.txt', 'r') as tfile:
            for line in tfile:
                author, title = line.split('\t')
                row = make_row(author, title)
                writer.writerow(row)
