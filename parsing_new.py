"""" parsing new s funksiami """

from bs4 import BeautifulSoup
import requests
import csv

URL = "https://kloop.kg/"
def get_html(url: str) -> str:
  response = requests.get(url)
  print(response.status_code)
  return response.text

html = get_html(URL)

def get_articles(html: str) -> list:
  soup = BeautifulSoup(html, "lxml")
  container = soup.find_all("div", class_="elementor-posts-container")[3]
  articles = container.find_all("article", class_="elementor-post")
  return articles

articles = get_articles(html)

def get_data(articles: list) -> None:
  for art in articles:
    try:
      img = art.find("img").get("src")
    except:
      img = ""

    try:
      title = art.find("h3", class_="elementor-post__title").text.strip()
    except:
      title = ""
    try:
      link = art.find("h3", class_="elementor-post__title").find('a').get("href")
    except:
      link = ""

    try:
      date = art.find("span", class_="elementor-post-date").text.strip()
    except:
      date = ""
    data = {
        "title": title,
        "image": img,
        "date": date,
        "link": link
    }
    write_to_csv(data)

    # print(img, title, date)
# get_data(articles)

def write_headers():
  with open("news.csv", "a") as f:
    columns = ["title", "image", "date", "link"]
    writer = csv.DictWriter(f, fieldnames=columns)
    writer.writeheader()

def write_to_csv(data: dict) -> None:
  with open("news.csv", "a") as f:
    columns = ["title", "image", "date", "link"]
    writer = csv.DictWriter(f, fieldnames=columns)
    writer.writerow(data)

write_headers()
get_data(articles)
len(articles)

def get_last_page(html: str) -> int:
  soup = BeautifulSoup(html, "lxml")
  pages = soup.find("nav", class_="elementor-pagination").find_all("a")[-2].text.strip()[-1]
  return int(pages)
get_last_page(html)

def main(url: str) -> None:
  html = get_html(url)
  last_page = get_last_page(html)
  write_headers()
  for page in range(1, last_page+1):
    #           https://kloop.kg/page/1/
    url_page = f"{url}page/{page}/"
    html_page = get_html(url_page)
    articles = get_articles(html_page)
    get_data(articles)

main(URL)
