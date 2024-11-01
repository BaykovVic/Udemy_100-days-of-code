from bs4 import BeautifulSoup
import lxml

with open("website.html") as file:
    content = file.read()

soup = BeautifulSoup(content, "html.parser")
print(soup.title.string)
all_anchor_tags = soup.find_all(name="a")
print(all_anchor_tags)

for tag in all_anchor_tags:
    print(tag.get("href"))

heading = soup.find(name="h1", id="name")
print(heading.get_text())

section_heading = soup.find(name="h3", class_="heading")
print(section_heading.get_text())

company_url = soup.select_one(selector="p a")
print(company_url.get("href"))

name = soup.select_one(selector="#name")
print(name.get_text())

headings = soup.select(".heading")
print(headings)