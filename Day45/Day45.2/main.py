from bs4 import BeautifulSoup
import requests

URL = "https://news.ycombinator.com/news"

response = requests.get(URL)
soup = BeautifulSoup(response.text, "html.parser")
link_spans = soup.find_all("span", class_="titleline")
print(link_spans)
for span in link_spans:
    anchor = span.find("a")
    print(anchor.get_text())

