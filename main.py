import httpx
from selectolax.parser import HTMLParser
from saveToTxt import save_to_file

url = 'https://www.bookmarked.club/people/peter-thiel'
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 OPR/104.0.0.0"}
resp = httpx.get(url, headers=headers)
html = HTMLParser(resp.text)

def extract_text(html, sel): #consider the scenario where one of the fields might be empty
    try:
        return html.css_first(sel).text()
    except AttributeError:
        return None

books = html.css("div.bottom-row")
recomendedBooks = []
for book in books:
    recomendedBooks.append({
        "title": extract_text(book, ".list-heading"),
        "author": extract_text(book, ".book-page-subheading")
    })
save_to_file(recomendedBooks)
print(recomendedBooks)



