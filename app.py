from trywebscraping import Fetch

hn = Fetch("https://news.ycombinator.com")
articles = hn.query("tr.athing").extract({
    "rank": "span.rank",
    "title": "td.title a",
    "link": "td.title a@href"
}).limit(10)
print(articles)