#2024/11/01:大場史温

import requests

def get_formatted_address_fromKeyWord(keyWord):

    #APIブロックされるのでヘッダー必要
    headers = {
    "User-Agent": "ReitakuUniv"
    }

    #OSMのエンドポイント
    url = "https://nominatim.openstreetmap.org/search"
    
    params = {
        'q': keyWord,
        'format': 'json',
        'addressdetails': 1
    }
    
    response = requests.get(url, headers=headers, params=params)
    
    print("Request URL:", response.url)
    
    try:
        results = response.json()
        
        if results:
            #DisplayNameの値を取得
            formatted_address = results[0]['display_name']
            print("フォーマットされた住所:", formatted_address)
            return formatted_address
        else:
            return None
    except requests.exceptions.JSONDecodeError:
        print("レスポンスがJSON形式ではありません。")
        print("レスポンス内容:", response.text)
        return None
    

def get_formatted_address_fromKeyLatLnag(Lat,Lng):

    #APIブロックされるのでヘッダー必要
    headers = {
    "User-Agent": "ReitakuUniv"
    }

    #OSMのエンドポイント
    url = "https://nominatim.openstreetmap.org/reverse"
    
    params = {
        'lat': Lat,
        'lon': Lng,
        'format': 'json',
        'addressdetails': 1
    }
    
    response = requests.get(url, headers=headers, params=params)
    
    print("Request URL:", response.url)
    
    try:
        results = response.json()
        
        if results:
            #DisplayNameの値を取得
            formatted_address = results['display_name']
            print("formatted_address:", formatted_address)
            return formatted_address
        else:
            return None
    except requests.exceptions.JSONDecodeError:
        print("jsonじゃない")
        print("Res:", response.text)
        return None
    
    
