from scrapEmoji import emojiScaper

import json

with open('categoryDetails.json') as json_file:
    data = json.load(json_file)

# ## for debug purpose
# obj1 =                {
#                     "emoji": "\ud83d\ude00",
#                     "name": "Grinning Face",
#                     "url": "/grinning-face/"
#                 }
# emojiScaper(data['home'], obj1['url'])
# ## debug purpose ends


with open('emojisInCategory.json') as json_file:
    categories = json.load(json_file)

finalList = []
errorList = []

for categ in categories['catEmojiList']:
    print(categ['category'])
    for emObj in categ['emojiList']:
        try:
            finalList.append(emojiScaper(data['home'], emObj['url']))
        except:
            print("== == == == == == == == == == == == == == == ==")
            errorList.append(emObj['url'])

dump_obj = {
    'emojiDetailList' : finalList,
    'errorList' : errorList
}

with open('emojiDetailsImages-4.json', 'w') as outfile:
    json.dump(dump_obj, outfile, indent = 4, sort_keys=True)

print(errorList)