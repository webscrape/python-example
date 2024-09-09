from trywebscraping import Fetch

# hn = Fetch("https://news.ycombinator.com")
hn = Fetch("https://this-is-an-invalid-site.com")
articles = hn.query("tr.athing").extract({
    "rank": "span.rank",
    "title": "td.title a",
    "link": "td.title a@href"
}).limit(10)
print(articles)