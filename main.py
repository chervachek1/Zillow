import csv
import json
import urllib.parse

import requests


def get_data():

    zips_list = []

    link = 'https://www.zillow.com/search/GetSearchPageState.htm?'

    for page in range(1, 5):
        params = {
            'searchQueryState': {
                "pagination":
                    {"currentPage": page},
                "usersSearchTerm":
                    "Jacksonville, FL",
                "mapBounds":
                    {"west": -82.15106542675781,
                     "east": -81.22684057324219,
                     "south": 29.975416146834,
                     "north": 30.70903560923411},
                "regionSelection":
                    [{"regionId": 25290, "regionType": 6}],
                "isMapVisible": True
                ,
                "filterState":
                    {"isAllHomes":
                         {"value": True
                          },
                     "hasPool":
                         {"value": True
                          },
                     "sortSelection":
                         {"value": "globalrelevanceex"}
                     },
                "isListVisible": True
            },
            'wants': {"cat1": ["listResults"]},
            'requestId': 2
        }

        with requests.Session() as s:
            s.headers[
                'User-Agent'] = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'
            s.headers["x-requested-session"] = "BE6D8DA620E60010D84B55EB18DC9DC8"
            s.headers["cookie"] = f"JSESSIONID={s.headers['x-requested-session']}"
            data = json.loads(s.get(f"{link}{urllib.parse.urlencode(params)}").content)

            for item in data.get('cat1').get('searchResults').get('listResults'):
                zips_list.append(item.get('zpid'))
    return zips_list


def get_full_data():

    zips_list = get_data()
    for zipd in zips_list:

        headers = {
            'authority': 'www.zillow.com',
            'accept': '*/*',
            'accept-language': 'uk,ru;q=0.9,uk-UA;q=0.8,en-US;q=0.7,en;q=0.6,he;q=0.5',
            'client-id': 'home-details_fs-sp_bootstrap',
            # Already added when you pass json=
            # 'content-type': 'application/json',
            # Requests sorts cookies= alphabetically
            # 'cookie': f"zguid=24|%2475b50303-985d-488f-92a9-015d002d5c6a; zgsession=1|326b0632-2d41-4106-876c-b06f06ee23b9; _ga=GA1.2.1183112601.1655662106; _gid=GA1.2.414231529.1655662106; zjs_user_id=null; zg_anonymous_id=%2208929b55-1bf5-4d12-a795-b61e935cbf5a%22; zjs_anonymous_id=%2275b50303-985d-488f-92a9-015d002d5c6a%22; _pxvid=d0b35a39-effa-11ec-8322-4872586a5548; pxcts=d0b367c6-effa-11ec-8322-4872586a5548; _gcl_au=1.1.620712197.1655662107; KruxPixel=true; DoubleClickSession=true; __pdst=4390163c0da148e7bb84013e76f64771; _cs_c=0; _hp2_id.1215457233=%7B%22userId%22%3A%228749776841928615%22%2C%22pageviewId%22%3A%228019728425887786%22%2C%22sessionId%22%3A%223122848270027128%22%2C%22identity%22%3Anull%2C%22trackerVersion%22%3A%224.0%22%7D; _cs_id=9ec93813-c163-ab0b-a930-9769204ba77f.1655662107.1.1655662107.1655662107.1.1689826107931; _pin_unauth=dWlkPVl6bGtNR05qWVRBdFpEUm1ZaTAwT0RSaExXRTRNR010TmpFeU16a3hPR1U1Tm1Waw; _clck=1rqdven|1|f2g|0; utag_main=v_id:01817d26da7b001ede51ad650cf20506f001706700978{_sn:1$_se:1$_ss:1$_st:1655663907260$ses_id:1655662107260%3Bexp-session$_pn:1%3Bexp-session$dcsyncran:1%3Bexp-session$tdsyncran:1%3Bexp-session$dc_visit:1$dc_event:1%3Bexp-session$dc_region:eu-central-1%3Bexp-session;} KruxAddition=true; _gat=1; _pxff_bsco=1; JSESSIONID=0C3E1106AF841C0515435E7B8B6C296E; _px3=b7e160e90819a1ca516f0bd0d46ef59144779bdea171b40bbef29fbebb10d7e4:77zBJ1gy01TdWchIpflkOc18poylXZSref82Cq30YQzZ/n2QwU8xv6TQ99tiq14cDtfhGcBs+c7z7PytaCkvLA==:1000:FRa2/H7s54qat7E0rF4LreveKSZ+554XZqhQ+NMkzdR1prlbngFtjCbhAXeuqW2owR4NPZOXG4v6IDGQNb7O6QCqPpxJrywWpbZoLetDGEA8mXzpe+fM0R4P1Ubm2uMHeqC1uFhOnOe5KVom+h3jcEO0yqjul9dor3/17JpBh9cyvXXwnHIFco66Py4/67YqEU3+pKS62C7UmYf+RxaAng==; _uetsid=d14cb340effa11ec8c8b33805c7a264c; _uetvid=d14cc050effa11eca866e1d9fed4d516; AWSALB=LSQWrZ/nwcrzMXFhHEpQKIBQBHwoOMRl/kp1x3U5veS3NKqsPO699dxuvvRliZIUiTP03ihyvysnXBZlFesqo0rWp5FZzCakYnxsoPdlzNZXxOpMDgTWagcG73C1; AWSALBCORS=LSQWrZ/nwcrzMXFhHEpQKIBQBHwoOMRl/kp1x3U5veS3NKqsPO699dxuvvRliZIUiTP03ihyvysnXBZlFesqo0rWp5FZzCakYnxsoPdlzNZXxOpMDgTWagcG73C1; search=6|1658264243949%7Crect%3D30.709035609234103%252C-81.22684057324219%252C29.975416146834007%252C-82.15106542675781%26rid%3D25290%26disp%3Dmap%26mdm%3Dauto%26p%3D4%26z%3D1%26fs%3D1%26fr%3D0%26mmm%3D0%26rs%3D0%26ah%3D0%26singlestory%3D0%26housing-connector%3D0%26abo%3D0%26garage%3D0%26pool%3D1%26ac%3D0%26waterfront%3D0%26finished%3D0%26unfinished%3D0%26cityview%3D0%26mountainview%3D0%26parkview%3D0%26waterview%3D0%26hoadata%3D1%26zillow-owned%3D0%263dhome%3D0%26featuredMultiFamilyBuilding%3D0%09%0925290%09%09%09%09%09%09; _clsk=ybkaqe|1655672246925|1|0|h.clarity.ms/collect; g_state={\"i_p\":1655679448006,\"i_l\":1}",
            'origin': 'https://www.zillow.com',
            'referer': 'https://www.zillow.com/homedetails/14254-Mount-Pleasant-Rd-Jacksonville-FL-32225/44584254_zpid/',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="102", "Google Chrome";v="102"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Windows"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-origin',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36',
        }

        params = {
            'zpid': f'{zipd}',
            'contactFormRenderParameter': '',
            'queryId': '798472f34ab197e0a28da2c65c8efec6',
            'operationName': 'ForSaleShopperPlatformFullRenderQuery',
        }

        json_data = {
            'operationName': 'ForSaleShopperPlatformFullRenderQuery',
            'variables': {
                'zpid': zipd,
                'contactFormRenderParameter': {
                    'zpid': zipd,
                    'platform': 'desktop',
                    'isDoubleScroll': True,
                },
            },
            'clientVersion': 'home-details/6.1.681.master.295a1d8',
            'queryId': '798472f34ab197e0a28da2c65c8efec6',
        }

        response = requests.post('https://www.zillow.com/graphql/', params=params, headers=headers, json=json_data).json()
        data = response['data']['property']
        street_address = data['address']['streetAddress']
        city = data['address']['city']
        state = data['address']['state']
        zipcode = data['address']['zipcode']
        country = data['country']
        bedrooms = data['bedrooms']
        bathrooms = data['bathrooms']
        price = data['price']
        yearBuilt = data['yearBuilt']
        livingAreaValue = f"{data['livingAreaValue']} {data['livingAreaUnitsShort']}"
        description = data['description']

        agentName = data['attributionInfo']['agentName']
        agentEmail = data['attributionInfo']['agentEmail']
        agentPhoneNumber = data['attributionInfo']['agentPhoneNumber']
        brokerName = data['attributionInfo']['brokerName']
        brokerPhoneNumber = data['attributionInfo']['brokerPhoneNumber']
        photoList = []
        for photo in data['photos']:
            photoList.append(photo['mixedSources']['jpeg'][-1]['url'])
        photo_list = ' ; '.join(photoList)

        with open('Example.csv', 'a', encoding='utf-8', newline='') as file:
            writer = csv.writer(file, delimiter=',')
            writer.writerow(
                [
                    street_address,
                    zipcode,
                    city,
                    state,
                    country,
                    bedrooms,
                    bathrooms,
                    livingAreaValue,
                    price,
                    yearBuilt,
                    description,
                    photo_list,
                    agentName,
                    agentEmail,
                    agentPhoneNumber,
                    brokerName,
                    brokerPhoneNumber
                ]
            )


def main():
    with open('Example.csv', 'w', encoding='utf-8', newline='') as file:
        writer = csv.writer(file, delimiter=',')
        writer.writerow(
            [
                'street_address',
                'zipcode',
                'city',
                'state',
                'country',
                'bedrooms',
                'bathrooms',
                'livingAreaValue',
                'price',
                'yearBuilt',
                'description',
                'photo_list',
                'agentName',
                'agentEmail',
                'agentPhoneNumber',
                'brokerName',
                'brokerPhoneNumber'
            ]
        )
    get_full_data()


if __name__ == '__main__':
    main()