#!/usr/bin/env python3
'''
This is a slow one, but works.
'''

import scholarly
import pandas as pd
from csv import DictWriter

def get_author_data(author):
    '''
    Gets metadata for a single author. 
    '''
    author_data = [] 
    print('Looking up:', author)    
    try: 
        a = scholarly.search_author(author)
    except Exception as e:
        print('Error with API call', e)
    while True: 
        try: 
            info = next(a) 
            print(info) 
            writer.writerow({'name': info.name
                           , 'id': info.id
                           , 'email': info.email}) 
        
        except StopIteration:
            break

if __name__ == "__main__":
    
    with open('researchers.txt') as f:
        researchers = [x.replace('\n', '').strip() for x in f.readlines()]

    with open('researches.csv', 'w', newline='') as csvfile:
        fieldnames = ['name', 'id', 'email']
        writer = DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for researcher in researchers:
            get_author_data(researcher)
