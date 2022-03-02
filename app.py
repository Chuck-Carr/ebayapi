import key
import datetime
from ebaysdk.exception import ConnectionError
from ebaysdk.finding import Connection
from bs4 import BeautifulSoup as bs

try:
    api = Connection(appid= key.api_key, config_file=None)
    response = api.execute('findItemsAdvanced', {'keywords': 'nike'})




    soup = bs(response.content, 'lxml')

    items = soup.find_all('item')
    length = len(items)
    print(length)
    
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

except:
    pass