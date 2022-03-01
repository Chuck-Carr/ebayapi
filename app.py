import key
from ebaysdk.exception import ConnectionError
from ebaysdk.finding import Connection
from bs4 import BeautifulSoup as bs

try:
    api = Connection(appid= key.api_key, config_file=None)
    response = api.execute('findItemsAdvanced', {'keywords': 'Nike Dunk Low 8.5'})
    

except ConnectionError as e:
    print(e)
    print(e.response.dict())


soup = bs(response.content, 'lxml')

items = soup.find_all('item')

for item in items:
    title = item.title.string.lower().strip()
    price = int(round(float(item.currentprice.string)))
    url = item.viewitemurl.string.lower()
    # seller = item.sellerusername.text.lower()
    cat = item.categoryname.string.lower()
    condition = item.conditiondisplayname.string.lower()

    if "new" in condition and price < 160:

        print(f"Title: {title}, Price: ${price}")
        print(f"Condition: {condition}")
        print(f"Link: {url}\n")