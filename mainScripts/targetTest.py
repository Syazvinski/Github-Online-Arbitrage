import json
import requests

headers = {
    "User-Agent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0"
}

api_url = "https://redsky.target.com/redsky_aggregations/v1/web/plp_search_v1"

#https://redsky.target.com/redsky_aggregations/v1/web/plp_search_v1?key=ff457966e64d5e877fdbad070f276d18ecec4a01&channel=WEB&count=24&default_purchasability_filter=true&include_sponsored=true&keyword=pink+plate&offset=0&page=%2Fs%2Fpink+plate&platform=desktop&pricing_store_id=1294&scheduled_delivery_store_id=1294&store_ids=1294%2C669%2C967%2C1497%2C1300&useragent=Mozilla%2F5.0+%28Macintosh%3B+Intel+Mac+OS+X+10_15_7%29+AppleWebKit%2F537.36+%28KHTML%2C+like+Gecko%29+Chrome%2F93.0.4577.63+Safari%2F537.36&visitor_id=017BB2485076020185748EA5E363C1E0

params = {
    "key": "ff457966e64d5e877fdbad070f276d18ecec4a01",
    "channel": "WEB",
    "count": "24",
    "default_purchasability_filter": "false",
    "include_sponsored": "true",
    "keyword": "pink plate",
    "offset": "0",
    "page": "/s/pink plate",
    "platform": "desktop",
    "pricing_store_id": "3991",
    "useragent": "Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:91.0) Gecko/20100101 Firefox/91.0",
    "visitor_id": "AAA",
}

data = requests.get(api_url, params=params).json()

# #uncomment this to print all data:
# f = open("targetResult.json", "a")
# f.write(json.dumps(data, indent=4))
# f.close()


for p in data["data"]["search"]["products"]:
    print(
        "{:<10} {}".format(
            p["price"]["current_retail"],
            p["item"]["product_description"]["title"],
        )
    )

