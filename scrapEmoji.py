import httplib2
from bs4 import BeautifulSoup
http = httplib2.Http()
import pprint

def emojiScaper(homeUrl, urlSlug):

    scrap = {}

    url = homeUrl + urlSlug[1:]
    status, response = http.request(url)
    soup = BeautifulSoup(response)
    # print(soup.article.prettify())

    # title: [emoji and title]
    articleNode = soup.article
    H_1 = articleNode.h1
    # print(H_1)
    scrap['emoji'] = H_1.span.text
    # print(H_1.span.text, end=" ")
    H_1.span.decompose()
    scrap['title'] = H_1.text.strip()
    print(H_1.text.strip(), end="|")

    # description in HTML format
    sectionNode = articleNode.find('section',{'class':['description']})
    sectionNode.h2.decompose()
    sectionNode.form.decompose()
    sectionNode.h2.decompose()
    pNodes = sectionNode.findAll('p')
    InfoList = [pNode.text.strip() for pNode in pNodes]
    # for aLine in InfoList:
    #     print(">>",aLine)
    scrap['description'] = InfoList
    # print(sectionNode.prettify())

    ## aliases
    aliasesLst = []
    try:
        sectionNode = articleNode.find('section',{'class':['aliases']})
        sectionNode.h2.decompose()
        for spanNode in sectionNode.findAll('span'):
            spanNode.decompose()
        # for liNode in sectionNode.findAll('li'):
        #     print(liNode.text.strip())  
        aliasesLst = [liNode.text.strip() for liNode in sectionNode.findAll('li')]
    except:
        print("No aliases.")
    scrap['aliases'] = aliasesLst

    ## applenames
    sectionNode = articleNode.find('section',{'class':['applenames']})
    if sectionNode:
        sectionNode.h2.decompose()
        sectionNode.span.decompose()
        # print(sectionNode.p.text.strip())
        scrap['applenames'] = sectionNode.p.text.strip()
    else:
        scrap['applenames'] = "-"

    ## unicodename
    sectionNode = articleNode.find('section',{'class':['unicodename']})
    if sectionNode:
        sectionNode.h2.decompose()
        sectionNode.span.decompose()
        # print(sectionNode.p.text.strip())
        scrap['unicodename'] = sectionNode.p.text.strip()
    else:
        scrap['unicodename'] = "-"

    ## scraping images
    sectionNode = articleNode.find('section',{'class':['vendor-list']})
    allLi = sectionNode.findAll('div',{'class':['vendor-rollout-target']})
    scrap['images'] = []

    # print(len(allLi))
    for Li in allLi:
        img_obj = {}
        img_obj["platform"] = (Li.h2.text)
        theImage = Li.img
        img_obj["img_src"] = (theImage['src'])
        img_obj["img_alt"] = (theImage['alt'])
        scrap['images'].append(img_obj)

    ## vendor-list decomposition
    for secNode in articleNode.find_all('section'):
        secNode.decompose()

    ### Codepoints

    H_2list = articleNode.find_all('h2')
    # print("h2 debug start\n",[node.text for node in H_2list],"h2 debug end")

    codeNode = H_2list[0]
    # print(codeNode.text)
    codeUL = codeNode.find_next_sibling()
    scrap['codepoints'] = [liObj.text[2:] for liObj in codeUL.find_all('li')]
    # print(scrap['codepoints'])

    ### Shortcodes

    codeNode = H_2list[1]
    if codeNode.text == "Shortcodes":
        # print(codeNode.text)
        codeUL = codeNode.find_next_sibling()
        # print(codeUL.prettify())
        shortcodesList = []
        for eachLi in codeUL.find_all('li'):
            shortcodes = {}
            shortcodes['code'] = eachLi.span.text
            paltForms = []
            for aNode in eachLi.find_all('a'):
                paltForms.append(aNode.text)
            # print(paltForms)
            shortcodes['platforms'] = paltForms
            shortcodesList.append(shortcodes)
        scrap['shortcodes'] = shortcodesList
    else:
        scrap['shortcodes'] = []

    ### SeeAlso...

    seeAlsoNode = H_2list[2]
    # print(seeAlsoNode.text)
    liList = seeAlsoNode.find_next_sibling().findAll('li')

    emojiList = []

    # print(liList)

    for node in liList:
        try:
            emoji = {}
            emoji['emoji'] = node.span.text
            node.span.decompose()
            emoji['name'] = node.text.strip()
            emoji['url'] = node.a['href']
            emojiList.append(emoji)
        except:
            print("Error in ...")
            print(node)

    scrap['seeAlso'] = emojiList

    ### Adding id/url-slug

    scrap['id'] = urlSlug[1:-1]

    # for key in scrap.keys():
    #     print("-- -- -- --")
    #     print(key)
    #     print(scrap[key])

    return(scrap)
