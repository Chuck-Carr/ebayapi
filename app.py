from multiprocessing import connection
import key
import datetime
from ebaysdk.exception import ConnectionError
from ebaysdk.finding import Connection
from bs4 import BeautifulSoup as bs
import pandas as pd

# try:
#     api = Connection(appid= key.api_key, config_file=None)
#     response = api.execute('findItemsAdvanced', {'keywords': 'nike'})




#     soup = bs(response.content, 'lxml')

#     items = soup.find_all('item')
#     length = len(items)
#     print(length)
    
    # for item in items: 
    #     assert(response.reply.ack == 'Success')
    #     assert(type(response.reply.timestamp) == datetime.datetime)
    #     assert(type(response.reply.searchResult.item) == list)

    #     item = response.reply.searchResult.item[0]
    #     assert(type(item.listingInfo.endTime) == datetime.datetime)
    #     assert(type(response.dict()) == dict)
    #     item_endTime = item.listingInfo.endTime.strftime("%H:%M:%S")
    #     item_endDate = item.listingInfo.endTime.strftime("%Y-%m-%d")

        # print(item.listingInfo.endTime)
        # print(f"{item_endDate} {item_endTime}")
        # print(datetime.datetime.now())

        # date_2 = item.listingInfo.endTime
        # date_1 = datetime.datetime.now()

        # time_delta = (date_2 - date_1)
        # total_seconds = time_delta.total_seconds()
        # minutes = total_seconds/60

        # if minutes < 1500:
            # print(item)

        # if minutes > 1440:
        #     print(item)



        # print(f"End date is: {item_endDate}")
        # print(f"End time is: {item_endTime}\n")
    # print(item.listingInfo.endTime)
    # date_1 = item.listingInfo.endTime
    # date_2 = datetime.datetime.now()
    # # print(datetime.datetime.now())
    
    # time_delta = (date_2 - date_1)
    # total_seconds = time_delta.total_seconds()
    # minutes = total_seconds/60

    # print(minutes)
# except ConnectionError as e:
#     print(e)
#     print(e.response.dict())


# soup = bs(response.content, 'lxml')

# items = soup.find_all('item')

# for item in items:
#     title = item.title.string.lower().strip()
#     price = int(round(float(item.currentprice.string)))
#     url = item.viewitemurl.string.lower()
#     # seller = item.sellerusername.text.lower()
#     cat = item.categoryname.string.lower()
#     condition = item.conditiondisplayname.string.lower()

#     time = datetime.datetime.now()

#     assert(type(item.endtime) == datetime.datetime)

#     # end = item.endti
#     # me
#     print(item.endtime.text)
    # print(time)



    # if "new" in condition and price < 160:

    #     print(f"Title: {title}, Price: ${price}")
    #     print(f"Condition: {condition}")
    #     print(f"Link: {url}\n")

payload = {
        'keywords': 'nike dunk low 8.5', 
        'itemFilter': [
            {'name': 'LocatedIn', 'value': 'US'},
        ],
        'sortOrder': 'StartTimeNewest',
}

def get_results(payload):

    try:
        api = Connection(appid=key.api_key, config_file=None)
        response = api.execute('findItemsAdvanced', payload)
        return response.dict()

    except ConnectionError as e:
        print(e)
        print(e.response.dict())



def get_total_pages(results):
    if results:
        return int(results.get('paginationOutput').get('totalPages'))
    else:
        return


def search_ebay(payload):
    
    results = get_results(payload)
    total_pages = get_total_pages(results)
    items_list = results['searchResult']['item']
        
    i = 2
    while(i <= total_pages):
        payload['paginationInput'] = {'entriesPerPage': 100, 'pageNumber': i}        
        results = get_results(payload)
        items_list.extend(results['searchResult']['item'])
        i += 1
        
    df_items = pd.DataFrame(columns=['itemId', 'title', 'viewItemURL', 'galleryURL', 'location', 'postalCode',
                                 'paymentMethod','listingType', 'bestOfferEnabled', 'buyItNowAvailable',
                                 'currentPrice', 'bidCount', 'sellingState'])

    for item in items_list:
        row = {
            'itemId': item.get('itemId'),
            'title': item.get('title'),
            'viewItemURL': item.get('viewItemURL'),
            'galleryURL': item.get('galleryURL'),
            'location': item.get('location'),
            'postalCode': item.get('postalCode'),
            'paymentMethod': item.get('paymentMethod'),        
            'listingType': item.get('listingInfo').get('listingType'),
            'bestOfferEnabled': item.get('listingInfo').get('bestOfferEnabled'),
            'buyItNowAvailable': item.get('listingInfo').get('buyItNowAvailable'),
            'currentPrice': item.get('sellingStatus').get('currentPrice').get('value'),
            'bidCount': item.get('bidCount'),
            'sellingState': item.get('sellingState'),
        }
        left = item.get('sellingStatus').get('timeLeft') #P0DT2H42M0S
        time_left = left.split('H')
        
        if "P0DT0H" in time_left:
            print(f"{item.get('title')}")
            print(f"Price: {item.get('sellingStatus').get('currentPrice').get('value')}")
            print(f"Time Left: {time_left}\n")

    return df_items


# df_items = search_ebay(payload)
# df_items = df_items.sort_values(by=['currentPrice'], ascending=True)
# print(df_items[['title', 'currentPrice', 'location']].head())

# print(df_items.sort_values(by=['currentPrice'])) 

search_ebay(payload) 