'''
ORM classes for the site:
    Dataset: A dataset and meta data containing
        - something ...
    Researcher: A researcher that has worked with a dataset
        - something ...

Nick Tallant - July '18
'''

class DataSet:
    def __init__(self, name='', acronymn='', description='', **kwargs):
        self._validate(name, description) 
        self.name = name
        self.acronymn = acronymn
        self.description = description
        self.snippet = 'Code Snippet' 
        self._other_attrs = self._parse_attrs(**kwargs)

    def _validate(self, name, description):
        '''Just checks for name and description,
        may have it validate data types later.'''
        if not name:
            raise Exception('DataSet must have name.')
        if not description:
            raise Exception('DataSet must have description.')

    def _parse_attrs(self, **kwargs):
        return

    def __repr__(self):
         return 'Name: ' + self.name + '\nDescription: ' + self.description

class Researcher:
    def __init__(self, name='', department='', affiliation='', **kwargs):
        self._validate(name, department, affiliation) 
        self.name = name
        self.department = department 
        self.affiliation = affiliation 
        self._other_attrs = self._parse_attrs(**kwargs)

    def _validate(self, name, department, affiliation):
        '''Just checks for name, department, and affiliation.
        May have it validate data types later.'''
        if not name:
            raise Exception('DataSet must have name.')
        if not department:
            raise Exception('DataSet must have department.')
        if not affiliation:
            raise Exception('DataSet must have affiliation.')

    def _parse_attrs(self, **kwargs):
        return

    def __repr__(self):
         return ('Name: ' + self.name + '\n' + 
                 self.affiliation + ' at ' + self.department)
         
