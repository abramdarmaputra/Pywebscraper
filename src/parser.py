from bs4 import BeautifulSoup

def parse_quotes(html: str):
    soup = BeautifulSoup(html, "lxml")
    items = []
    for q in soup.select("div.quote"):
        text = q.select_one("span.text").get_text(strip=True).strip("“”")
        author = q.select_one("small.author").get_text(strip=True)
        tags = [t.get_text(strip=True) for t in q.select("div.tags a.tag")]
        items.append({"text": text, "author": author, "tags": tags})
    return items
    