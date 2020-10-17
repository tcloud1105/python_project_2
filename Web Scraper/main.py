from bs4 import BeautifulSoup
import requests

def startSearch:

search = input("Enter your search term: ")
params = {"q":search}
r = requests.get("http://www.bing.com/search", params=params)

soup = BeautifulSoup(r.text,'html.parser')
#print(soup.prettify())

results = soup.find("ol", {'id':"b_results"})
links = results.findAll('li', {'class':'b_algo'})

for item in links:
    item_text = item.find('a').text
    item_href = item.find('a').attrs['href']

    if item_text and item_href:
        print(item_text)
        print(item_href)
        print('Parent: ', item.find('a').parent)
        print('Summary: ', item.find('a').parent.parent.find('p').text)
        children = item.children
        for child in children:
            print('Child', child)

        firstchild = item.find('h2')
        print("Next Sibling of the h2: ", firstchild.next_sibling)
