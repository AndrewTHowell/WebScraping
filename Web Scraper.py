import requests
import lxml
import bs4

source = requests.get("https://devopscube.com/project-management-software").text

soup = bs4.BeautifulSoup(source, "lxml")

article = soup.find("article")

headline = article.div.h3.text

print(headline)
