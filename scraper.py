url = 'https://en.wikipedia.org/wiki/History_of_Mexico'
import requests
from bs4 import BeautifulSoup

def get_citations_needed_count(url):

    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    citations= soup.find_all('a',title="Wikipedia:Citation needed")
    print(f' "[Citation needed]" is repeated {len(citations)} times' , '\n ===================================')



def get_citations_needed_report(url):

    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    citations= soup.find_all('a',title="Wikipedia:Citation needed")

    for citation in citations:
        paragraph = citation.find_parents('p')[0].text.strip()

        print(paragraph , '\n ____________________________________________________________________')

get_citations_needed_count(url)
get_citations_needed_report(url)