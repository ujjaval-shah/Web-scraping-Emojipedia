import json
import httplib2
from bs4 import BeautifulSoup
http = httplib2.Http()

url = 'https://emojipedia.org/'
status, response = http.request(url)
soup = BeautifulSoup(response)

urlNodes = soup.find('div',{'class': 'block'}).findAll('a')

# for node in urlNodes:
#     print(node.text[0:1])
# # debug-purpose  

categories = [ {"emoji":node.text[:1], "category":node.text[2:], "url":node['href'] } for node in urlNodes]

person_dict = ({
    "categories": categories,
    "home": url
})

# print([i["category"][2:] for i in person_dict["categories"]])
# # debug-pupose

with open('categoryDetails.json', 'w') as outfile:
    json.dump(person_dict, outfile, indent = 4, sort_keys=True)