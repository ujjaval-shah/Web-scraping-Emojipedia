from scrapCategory import forACategory

import json
# import httplib2
# from bs4 import BeautifulSoup
# http = httplib2.Http()

with open('categoryDetails.json') as json_file:
    data = json.load(json_file)

catEmojiList = []

for cat_obj in data["categories"]:
    catEmojiList.append(forACategory(data['home'], cat_obj))
    print(cat_obj)

dump_obj = {
    "catEmojiList": catEmojiList
}

with open('emojisInCategory.json', 'w') as outfile:
    json.dump(dump_obj, outfile, indent = 4, sort_keys=True)
