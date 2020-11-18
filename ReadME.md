# Webscraping of EmojiPedia

**About:** Scripts to scrap emoji-pages of emojipedia.org

**Tools:** Python, BeautifulSoup4, json, IPython

## How to run

- Install required libraries

```bash
pip install beautifulsoup4
```

- Run the project

```bash
python scrapHomePage.py
python handler4Category.py
python handler4Emoji.py
```

## File: "emojiDetailsImages.json" updates

- ```description``` converted to Text instead of HTML nodes.
- Added ```images```
- inserted ```id```s for URL mapping
- structure of ```images``` changed
