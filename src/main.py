import requests
import json
import os
from datetime import datetime
from settings.config import LCBOConfig


headers = {
    'Authorization': f'Bearer {LCBOConfig.AUTH_TOKEN}',
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
}
payload = {
    'locale': 'en',
    'sortCriteria': '@ec_final_price ascending',
}

FILE_PATH = f"etc/files/drinks/{datetime.now().date()}"
if not os.path.exists(FILE_PATH):
    os.makedirs(FILE_PATH)

firstResult = 0
numberOfResults = 1000
price = 0
last_price = 0
while True:
    payload['firstResult'] = firstResult
    payload['numberOfResults'] = numberOfResults
    criteria = (f'@source==ProductsEN AND @enabled == true (@ec_visibility==(3,4)) (@cp_browsing_category_deny<>0) ('
                f'@ec_price=={price}..1000000)')
    payload['aq'] = criteria
    search_products_request = requests.post(LCBOConfig.LCBO_API_HOST, data=payload, headers=headers)

    products_response = search_products_request.json()

    if "totalCount" not in products_response:
        print(f"ERROR: {products_response}")

    if "results" not in products_response or len(products_response["results"]) == 0:
        print(f"DONE!!")
        break

    print(f"{firstResult} to {firstResult+numberOfResults} of {products_response['totalCount']} for price over {price}")
    for drink in products_response["results"]:
        drink_uniqueid = drink["UniqueId"].replace("/", "_")
        last_price = drink["raw"]["ec_final_price"]
        fileName = f"{FILE_PATH}/{drink_uniqueid}.json"
        if os.path.exists(fileName):
            print(f"FILE ALREADY EXISTS: {fileName}")
        with open(fileName, 'w') as file:
            file.write(json.dumps(drink, indent=4, sort_keys=True))
        file.close()

    firstResult += numberOfResults
    if firstResult + numberOfResults > LCBOConfig.MAX_RESULTS_RETURNED:
        firstResult = 0
        price = last_price
