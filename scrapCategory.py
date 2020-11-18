# Lists emojis given a category url

import httplib2
from bs4 import BeautifulSoup
http = httplib2.Http()

def forACategory(homeURL, catObj):
    url = homeURL + catObj['url'][1:]
    status, response = http.request(url)

    soup = BeautifulSoup(response)

    div_node = soup.find('div',{'class':'content'})

    title = div_node.h1
    # title.span.text
    title.span.decompose()
    # title.text.strip()

    liList = div_node.ul.find_all('li')

    emojiList = []

    for node in liList:
        emoji = {}
        emoji['emoji'] = node.span.text
        node.span.decompose()
        emoji['name'] = node.text.strip()
        emoji['url'] = node.a['href']
        emojiList.append(emoji)

    resultObj = {
        "category" : catObj['category'],
        "emojiList" : emojiList
    }

    return(resultObj)