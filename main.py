import httpx
from selectolax.parser import HTMLParser

url = 'https://www.kevinrooke.com/book-recommendations/peter-thiel'
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 OPR/104.0.0.0"}

resp = httpx.get(url, headers=headers)
html = HTMLParser(resp.text)
books = html.css("div.div-block-10")
recomendedBooks = []
for book in books:
    recomendedBooks.append({
        "name": book.css_first(".book-title").text(),
        "author": book.css_first(".heading-9").text()
    })

print(recomendedBooks)


