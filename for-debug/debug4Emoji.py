from scrapForEmoji import emojiScaper

import json

with open('categoryDetails.json') as json_file:
    data = json.load(json_file)

obj1 = {
    "emoji": "\ud83d\ude00",
    "name": "Grinning Face",
    "url": "/grinning-face/"
}


# for debug purpose
# obj1 =  {
#     "emoji": "\ud83c\udff4\udb40\udc75\udb40\udc73\udb40\udc74\udb40\udc78\udb40\udc7f",
#     "name": "Flag for Texas (US-TX)",
#     "url": "/flag-for-texas-ustx/"
# }
out = emojiScaper(data['home'], obj1['url'])
print(json.dumps(out, sort_keys=True, indent=4))
## debug purpose ends