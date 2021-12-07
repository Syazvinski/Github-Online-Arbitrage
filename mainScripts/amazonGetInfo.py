from requests_html import HTMLSession
import re

url = 'https://www.amazon.com/Mr-Coffee-Cappuccino-Stainless-Measuring/dp/B08NFMKHSK'

def getInfo(url):
    s = HTMLSession()
    r = s.get(url)
    r.html.render(timeout=30)

    try:
        weight = r.html.xpath('//*[@id="productDetails_detailBullets_sections1"]/tbody/tr[2]/td', first=True).text
    except:
        weight = "1 pound"

    try:
        size = r.html.xpath('//*[@id="productDetails_detailBullets_sections1"]/tbody/tr[1]/td', first=True).text
    except:
        size  = '12 x 12 x 12 inches'

    if 'pounds' in weight:
        weight = float(re.findall(r"[-+]?\d*\.\d+|\d+", weight)[0])*16
    elif 'ounces' in weight:
        weight = float(re.findall(r"[-+]?\d*\.\d+|\d+", weight)[0])

    amazonProduct = {
        'title': r.html.xpath('//*[@id="productTitle"]', first=True).text,
        'price': 19.98, #float(r.html.xpath('/html/body/div[1]/div[2]/div[8]/div[3]/div[4]/div[11]/div[1]/div/table/tbody/tr[2]/td[2]/span[1]/span[2]', first=True).text[1:]),
        'size': size
    }
    return amazonProduct

def wlmrtUrlGen(title):
    return 'https://walmart.com/search?query='+title.replace(" ",'%20')

if __name__ == "__main__":
    product = getInfo(url)
    print(wlmrtUrlGen(product['title']))