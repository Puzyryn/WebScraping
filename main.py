import requests
from bs4 import BeautifulSoup

# I have installed libraries such as BeautifulSoup and a requests

# A package for Web scraping of Google search results in Python.
"""
Created a function that will receive a keyword as an argument, load the Google search results page,
using requests and parse the results using BeautifulSoup. In the example below,
the function returns a list of titles and links to pages from the top 10 Google search results:
"""


def scrape_google_results(keyword):
    url = f'https://www.google.com/search?q={keyword}&num=10'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_0) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/78.0.3904.97 Safari/537.36'}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.text, 'html.parser')
    results = []
    for result in soup.find_all('div', {'class': 'g'}):
        link = result.find('a', href=True)
        title = result.find('h3')
        if link and title:
            results.append({'title': title.get_text(), 'link': link['href']})
    return results


results = scrape_google_results('Python tutorial')
print(results)
