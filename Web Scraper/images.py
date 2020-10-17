from bs4 import BeautifulSoup
import requests
from PIL import Image
from io import BytesIO
import os

def startSearch:

      search = input("Enter your search term: ")
      params = {"q":search}
      dirname = search.replace(' ', '_').lower()

      if not os.path.isdir(dirname):
          os.makedirs(dirname)
      r = requests.get("http://www.bing.com/search", params=params)

      soup = BeautifulSoup(r.text,'html.parser')
      links = soup.findAll('a', {'class':'thumb'})

     for item in links:
         try:
             img_obj = requests.get(item.attrs['href'])
             title = item.attrs['href'].split('/')[-1]
             try:
                 img = Image.open(BytesIO(img_obj.content))
                 img.save('./'+dirname+'/'+title, img.format)
             except:
                 print("I couldn't save image")
         except:
             print('could not request Image')
    startSearch()

startSearch()