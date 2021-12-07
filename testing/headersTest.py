from fake_useragent import UserAgent
import requests

from bs4 import BeautifulSoup

ua = UserAgent()
print(ua.chrome)
header = {'User-Agent':str(ua.chrome)}
print(header)

url = "https://www.amazon.com/s?k=lego&ref=nb_sb_noss_2"

reqs = requests.get(url, headers=header)

soup = BeautifulSoup(reqs.text, 'html.parser')

file = open("resp_text.txt", "w")
file.write(reqs.text)
file.close()

urls = []

for link in soup.find_all('a'):

    url = link.get('href')
    print(url)

    if '/B0' in str(url):
       urls.append(url)

print(urls)