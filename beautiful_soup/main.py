from bs4 import BeautifulSoup
import requests

# with open("website.html", mode="r", encoding="utf-8") as file:
#     contents = file.read()
#
# soup = BeautifulSoup(markup=contents, features="html.parser")
# all_anchors = soup.find_all(name="a")
#
# for tag in all_anchors:
#     print(f"{tag.getText()}: {tag.get('href')}")
#
# heading = soup.find(name="h1", id="name")
# print(heading)
#
# another_heading = soup.find(name="h3", class_="heading")
# print(another_heading)
#
# company_url = soup.select_one(selector="p a")
# print(company_url)
#
# main_heading = soup.select_one(selector="#name")
# print(main_heading)
#
# headings = soup.select(selector=".heading")
# print(headings)

response = requests.get("https://news.ycombinator.com/")
response.raise_for_status()
contents = response.text

soup = BeautifulSoup(markup=contents, features="html.parser")
story_links = soup.find_all(name="a", class_="storylink")

article_texts = []
article_links = []

for link in story_links:
    article_links.append(link.get("href"))
    article_texts.append(link.getText())

article_scores = [int(score.getText().split()[0]) for score in soup.find_all(name="span", class_="score")]
max_score = max(article_scores)
index_max_score = article_scores.index(max_score)
print(article_texts[index_max_score])
print(article_links[index_max_score])
print(max_score)