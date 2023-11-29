import httpx
from selectolax.parser import HTMLParser
from saveToTxt import save_to_file
from data_cleaning import remove_duplicates

url = ['https://www.bookmarked.club/people/warren-buffett', 'https://www.bookmarked.club/people/bill-ackman']
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36 OPR/104.0.0.0"}


def extract_text(html, sel): #consider the scenario where one of the fields might be empty
    try:
        return html.css_first(sel).text()
    except AttributeError:
        return None


recomendedBooks = []
for item in url:
    resp = httpx.get(item, headers=headers)
    html = HTMLParser(resp.text)
    books = html.css("div.bottom-row")
    for book in books:
        recomendedBooks.append({
            "title": extract_text(book, ".list-heading"),
            "author": extract_text(book, ".book-page-subheading")
        })
recomended_books_clean = remove_duplicates(recomendedBooks)
save_to_file(recomended_books_clean)



