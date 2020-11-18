from scrapForEmoji import emojiScaper

import json

with open('data.json') as json_file:
    data = json.load(json_file)

# ## for debug purpose
# obj1 =                {
#                     "emoji": "\ud83d\ude00",
#                     "name": "Grinning Face",
#                     "url": "/grinning-face/"
#                 }
# emojiScaper(data['home'], obj1['url'])
# ## debug purpose ends


remainingList = ['/smiling-face-with-tear/', '/disguised-face/', '/person-feeding-baby/', '/black-cat/', '/bison/', '/mammoth/', '/beaver/', '/polar-bear/', '/dodo/', '/feather/', '/seal/', '/beetle/', '/cockroach/', '/fly/', '/worm/', '/blueberries/', '/olive/', '/bell-pepper/', '/flatbread/', '/tamale/', '/fondue/', '/teapot/', '/bubble-tea/', '/accordion/', '/long-drum/', '/nesting-dolls/', '/sewing-needle/', '/coin/', '/carpentry-saw/', '/screwdriver/', '/hook/', '/ladder/', '/plunger/', '/mouse-trap/', '/bucket/', '/toothbrush/', '/left-speech-bubble/', '/female-sign/', '/male-sign/', '/transgender-flag/', '/flag-bouvet-island/', '/flag-clipperton-island/', '/flag-diego-garcia/', '/flag-ceuta-melilla/', '/flag-heard-mcdonald-islands/', '/flag-st-martin/', '/flag-svalbard-jan-mayen/', '/flag-tristan-da-cunha/', '/flag-us-outlying-islands/', '/flag-for-texas-ustx/']

finalList = []
errorList = []


for uRL in remainingList:
    # try:
        finalList.append(emojiScaper(data['home'], uRL))
    # except:
    #     print("== == == == == == == == == == == == == == == ==")
    #     errorList.append(uRL)

dump_obj = {
    'emojiDetailList' : finalList,
    'errorList' : errorList
}

with open('emojiDetail.json', 'w') as outfile:
    json.dump(dump_obj, outfile, indent = 4, sort_keys=True)

print(errorList)

