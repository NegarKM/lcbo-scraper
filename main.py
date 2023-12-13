import requests
import json
import os
from datetime import datetime

# auth_id: str = "30072"
# info_url = (
#     f"https://api.bazaarvoice.com/data/products.json?resource=products&filter=id%3Aeq%3A{auth_id}&filter_reviews"
#     f"=contentlocale%3Aeq%3Aen*%2Cfr*%2Cen_CA%2Cen_CA&filter_reviewcomments=contentlocale%3Aeq%3Aen*%2Cfr*%2Cen_CA"
#     f"%2Cen_CA&filteredstats=Reviews&stats=Reviews%2C+questions%2C+answers&passkey"
#     f"=caahDvc5HaPpIOIf7KgmpERQQPP3KRTtIKrSMQYpWz8MM&apiversion=5.5&displaycode=10862-en_ca")
#
# info_request = requests.get(info_url)
#
# info_response = info_request.json()

# print(json.dumps(info_response, indent=4))

# review_url= (f'https://api.bazaarvoice.com/data/reviews.json?resource=reviews&action=REVIEWS_N_STATS&filter=productid'
#               f'%3Aeq%3A{auth_id}&filter=contentlocale%3Aeq%3Aen*%2Cfr*%2Cen_CA%2Cen_CA&filter=isratingsonly%3Aeq'
#               f'%3Afalse&filter_reviews=contentlocale%3Aeq%3Aen*%2Cfr*%2Cen_CA%2Cen_CA&include=authors%2Cproducts'
#               f'&filteredstats=reviews&Stats=Reviews&limit=8&offset=0&sort=submissiontime%3Adesc&passkey'
#               f'=caahDvc5HaPpIOIf7KgmpERQQPP3KRTtIKrSMQYpWz8MM&apiversion=5.5&displaycode=10862-en_ca')
#
# review_request = requests.get(review_url)
#
# review_response = review_request.json()

# print(json.dumps(review_response, indent=4))

url = "https://platform.cloud.coveo.com/rest/search/v2?organizationId=lcboproductionx2kwygnc"
headers = {
    'Authorization': 'Bearer xx883b5583-07fb-416b-874b-77cce565d927',
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8',
    # 'Content-Length': '9483',
    # 'Origin': 'https://www.lcbo.com',
    # 'Referer': 'https://www.lcbo.com/en/products/wine/red-wine',
    # ':authority': 'platform.cloud.coveo.com', ':method': 'POST', ':path':
    # '/rest/search/v2?organizationId=lcboproductionx2kwygnc', ':scheme': 'https', "Sec-Ch-Ua": "Not/A)Brand";v="99",
    # "Google Chrome";v="115", "Chromium";v="115", 'Sec-Ch-Ua-Mobile": "?0", "Sec-Ch-Ua-Platform": "macOS",
    # "Sec-Fetch-Dest": "empty", "Sec-Fetch-Mode": "cors", "Sec-Fetch-Site": "cross-site", "User-Agent": "Mozilla/5.0
    # (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
}
payload = {
    'locale': 'en',
    # 'firstResult': 0,
    # 'numberOfResults': 10,
    # 'actionsHistory': [{"name":"Query","time":"\"2023-11-21T03:46:11.095Z\""},{"name":"Query",
    # "time":"\"2023-11-21T03:41:20.032Z\""},{"name":"Query","value":"impress",
    # "time":"\"2023-11-20T23:43:59.107Z\""},{"name":"Query","value":"chateau",
    # "time":"\"2023-11-20T23:29:10.176Z\""},{"name":"Query","time":"\"2023-11-20T23:29:00.947Z\""},{"name":"Query",
    # "time":"\"2023-11-20T19:20:51.055Z\""},{"name":"Query","value":"chateau",
    # "time":"\"2023-11-20T18:46:22.649Z\""},{"name":"Query","value":"dreaming tree",
    # "time":"\"2023-11-20T18:45:40.457Z\""},{"name":"Query","time":"\"2023-11-20T18:45:16.585Z\""},{"name":"Query",
    # "time":"\"2023-11-20T18:42:07.258Z\""},{"name":"Query","time":"\"2023-11-20T18:41:06.863Z\""},{"name":"Query",
    # "time":"\"2023-11-20T18:36:46.123Z\""}], 'analytics': {"clientId":"8f1cca80-3e0a-7173-2012-bf59d62cbee0",
    # "documentLocation":"https://www.lcbo.com/en/products/wine/red-wine#t=clp-products-wine-red_wine&sort=relevancy
    # &layout=card","documentReferrer":"","pageId":"","actionCause":"interfaceLoad","customData":{
    # "JSUIVersion":"2.10095.4;2.10095.4","context_website":"lcbo","context_langage":"en","website":"lcbo",
    # "siteName":"LCBO"},"originContext":"Search"},
    # 'visitorId': '8f1cca80-3e0a-7173-2012-bf59d62cbee0',
    # 'isGuestUser': False,
    # 'aq': '(@ec_category==Products) (@ec_visibility==(2,4)) (@cp_browsing_category_deny<>0) (@ec_price==0..100000)',
    # 'aq': '@source==ProductsEN AND @enabled == true (@ec_visibility==(3,4)) (@cp_browsing_category_deny<>0) (@ec_price==0..100000)',
    # 'cq': '@source==ProductsEN AND @enabled == true (@ec_visibility==(3,4)) (@cp_browsing_category_deny <>0)',
    # 'aq': '(@ec_visibility==(2,4)) (@cp_browsing_category_deny<>0) (@ec_category==Products)',
    # 'aq': '(@ec_visibility==(2,4)) (@cp_browsing_category_deny<>0) (@ec_category=="Products|Wine|Red Wine")',
    # 'searchHub': 'Web_Listing_EN',
    # 'tab': 'clp-products-wine-red_wine',
    # 'tab': 'Products',
    # 'excerptLength': 200,
    # 'enableDidYouMean': True,
    'sortCriteria': '@ec_final_price ascending',
    # 'queryFunctions': [],
    # 'rankingFunctions': [],
    # "groupBy": [{"field":"@lcbo_bintag_wine_sweetness","injectionDepth":10000,"computedFields":[{
    # "field":"@lcbo_bintag_wine_sweetness","operation":"minimum"},{"field":"@lcbo_bintag_wine_sweetness",
    # "operation":"maximum"}],"maximumNumberOfValues":1},{"field":"@lcbo_bintag_wine_body","injectionDepth":10000,
    # "computedFields":[{"field":"@lcbo_bintag_wine_body","operation":"minimum"},{"field":"@lcbo_bintag_wine_body",
    # "operation":"maximum"}],"maximumNumberOfValues":1},{"field":"@lcbo_bintag_wine_flavor_intensity",
    # "injectionDepth":10000,"computedFields":[{"field":"@lcbo_bintag_wine_flavor_intensity","operation":"minimum"},
    # {"field":"@lcbo_bintag_wine_flavor_intensity","operation":"maximum"}],"maximumNumberOfValues":1},
    # {"field":"@lcbo_bintag_wine_acidity","injectionDepth":10000,"computedFields":[{
    # "field":"@lcbo_bintag_wine_acidity","operation":"minimum"},{"field":"@lcbo_bintag_wine_acidity",
    # "operation":"maximum"}],"maximumNumberOfValues":1},{"field":"@lcbo_bintag_wine_tannins","injectionDepth":10000,
    # "computedFields":[{"field":"@lcbo_bintag_wine_tannins","operation":"minimum"},
    # {"field":"@lcbo_bintag_wine_tannins","operation":"maximum"}],"maximumNumberOfValues":1},{"field":"@ec_price",
    # "injectionDepth":10000,"computedFields":[{"field":"@ec_price","operation":"minimum"},{"field":"@ec_price",
    # "operation":"maximum"}],"maximumNumberOfValues":1},{"field":"@lcbo_total_volume","injectionDepth":10000,
    # "computedFields":[{"field":"@lcbo_total_volume","operation":"minimum"},{"field":"@lcbo_total_volume",
    # "operation":"maximum"}],"maximumNumberOfValues":1},{"field":"@lcbo_alcohol_percent","injectionDepth":10000,
    # "computedFields":[{"field":"@lcbo_alcohol_percent","operation":"minimum"},{"field":"@lcbo_alcohol_percent",
    # "operation":"maximum"}],"maximumNumberOfValues":1},{"field":"@lcbo_sugar_gm_per_ltr","injectionDepth":10000,
    # "computedFields":[{"field":"@lcbo_sugar_gm_per_ltr","operation":"minimum"},{"field":"@lcbo_sugar_gm_per_ltr",
    # "operation":"maximum"}],"maximumNumberOfValues":1}], "facets": [{"facetId":"@ec_category",
    # "field":"ec_category","type":"hierarchical","injectionDepth":1000,"delimitingCharacter":"|",
    # "filterFacetCount":True,"basePath":["Products","Wine","Red Wine"],"filterByBasePath":False,"currentValues":[],
    # "preventAutoSelect":False,"numberOfValues":5,"isFieldExpanded":False},{"facetId":"@lcbo_varietal_name",
    # "field":"lcbo_varietal_name","type":"specific","sortCriteria":"occurrences","injectionDepth":1000,
    # "filterFacetCount":True,"currentValues":[],"numberOfValues":5,"freezeCurrentValues":False,
    # "preventAutoSelect":False,"isFieldExpanded":False},{"facetId":"@lcbo_vqa_code","field":"lcbo_vqa_code",
    # "type":"specific","injectionDepth":1000,"filterFacetCount":True,"currentValues":[],"numberOfValues":8,
    # "freezeCurrentValues":False,"preventAutoSelect":False,"isFieldExpanded":False},
    # {"facetId":"@country_of_manufacture","field":"country_of_manufacture","type":"specific",
    # "sortCriteria":"occurrences","injectionDepth":1000,"filterFacetCount":True,"currentValues":[],
    # "numberOfValues":5,"freezeCurrentValues":False,"preventAutoSelect":False,"isFieldExpanded":False},
    # {"facetId":"@lcbo_region_name","field":"lcbo_region_name","type":"specific","sortCriteria":"occurrences",
    # "injectionDepth":1000,"filterFacetCount":True,"currentValues":[],"numberOfValues":5,
    # "freezeCurrentValues":False,"preventAutoSelect":False,"isFieldExpanded":False},{"facetId":"@lcbo_program",
    # "field":"lcbo_program","type":"specific","sortCriteria":"occurrences","injectionDepth":1000,
    # "filterFacetCount":True,"currentValues":[],"numberOfValues":5,"freezeCurrentValues":False,
    # "preventAutoSelect":False,"isFieldExpanded":False},{"facetId":"@lcbo_current_offer",
    # "field":"lcbo_current_offer","type":"specific","sortCriteria":"occurrences","injectionDepth":1000,
    # "filterFacetCount":True,"currentValues":[],"numberOfValues":8,"freezeCurrentValues":False,
    # "preventAutoSelect":False,"isFieldExpanded":False},{"facetId":"@stores_stock","field":"stores_stock",
    # "type":"specific","injectionDepth":1000,"filterFacetCount":True,"currentValues":[],"numberOfValues":8,
    # "freezeCurrentValues":False,"preventAutoSelect":False,"isFieldExpanded":False},{"facetId":"@ec_rating",
    # "field":"ec_rating","type":"numericalRange","sortCriteria":"descending","injectionDepth":1000,
    # "filterFacetCount":True,"currentValues":[{"start":1,"end":1.9,"endInclusive":True,"state":"idle"},{"start":2,
    # "end":2.9,"endInclusive":True,"state":"idle"},{"start":3,"end":3.9,"endInclusive":True,"state":"idle"},
    # {"start":4,"end":4.9,"endInclusive":True,"state":"idle"},{"start":5,"end":5,"endInclusive":True,
    # "state":"idle"}],"numberOfValues":5,"freezeCurrentValues":False,"generateAutomaticRanges":False}],
    # 'facetOptions': {},
    # 'categoryFacets': [],
    # 'retrieveFirstSentences': True,
    # 'timezone': 'America/Toronto',
    # 'enableQuerySyntax': False,
    # 'enableDuplicateFiltering': False,
    # 'enableCollaborativeRating': False,
    # 'debug': False,
    # 'allowQueriesWithoutKeywords': True,
    # 'q': 'dream' 'dictionaryFieldContext': {"stores_stock":"","stores_inventory":"217",
    # "stores_stock_combined":"217","stores_low_stock_combined":"217"}
}

FILE_PATH = f"etc/files/drinks/{datetime.now().date()}"
if not os.path.exists(FILE_PATH):
    os.makedirs(FILE_PATH)

firstResult = 0
numberOfResults = 100
price = 0
last_price = 0
while True:
    payload['firstResult'] = firstResult
    payload['numberOfResults'] = numberOfResults
    criteria = (f'@source==ProductsEN AND @enabled == true (@ec_visibility==(3,4)) (@cp_browsing_category_deny<>0) ('
                f'@ec_price=={price}..1000000)')
    payload['aq'] = criteria
    search_products_request = requests.post(url, data=payload, headers=headers)

    products_response = search_products_request.json()

    if "totalCount" not in products_response:
        print(f"ERROR: {products_response}")

    if "results" not in products_response or len(products_response["results"]) == 0:
        print(f"DONE. firstResult: {firstResult}, numberOfResults:{numberOfResults} -> {products_response}")
        break

    print(f"{firstResult} to {firstResult+numberOfResults} of {products_response['totalCount']} for price over {price}")
    # summary = []
    for drink in products_response["results"]:
        # drink_title = drink["title"].replace("/", "_")
        # drink_id = drink["raw"]["permanentid"]
        drink_uniqueid = drink["UniqueId"].replace("/", "_")
        last_price = drink["raw"]["ec_final_price"]
        fileName = f"{FILE_PATH}/{drink_uniqueid}.json"
        file = open(fileName, "w+")
        # res = {
        #     "title": drink_title,
        #     "uri": drink["uri"],
        #     "id": drink_id,
        # }
        file.write(json.dumps(drink, indent=4, sort_keys=True))
        file.close()
        # summary.append(res)

    # print(json.dumps({"result": summary}, indent=4))
    firstResult += numberOfResults
    if firstResult + numberOfResults > 5000:
        firstResult = 0
        price = last_price
