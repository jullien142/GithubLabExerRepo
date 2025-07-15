from bs4 import BeautifulSoup
soup = BeautifulSoup(html_doc, 'html.parser')

soup.find(name=None, attrs={}, recursive=True, string=None, **kwargs)

soup.find_all(name=None, attrs={}, recursive=True, string=None, limit=None, **kwargs)
