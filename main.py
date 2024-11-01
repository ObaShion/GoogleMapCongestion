#2024/11/01:大場史温

import livepopulartimes
import osmAPI
import time
import csv
import matplotlib.pyplot as plt
import folium


if __name__ == "__main__":
    
    #場所
    queries = [
               [35.863169790851025, 139.96882473556482],
               [35.86117478603994, 139.97304899384798],
               [35.86098004101116, 139.97279681962127],
               [35.8612356950586, 139.97200975213113],
               [35.86038529928114, 139.97336559998251],
               [35.86224376868518, 139.96894799323556],
               ]
                   
                   #金曜日の18時～21時の混雑度
                   dinner_time_popularity = {}

for query in queries:
    
    query_tuple = tuple(query)
        
        # フォーマットされた住所を取得しformatted_addressに追加
        formatted_address = osmAPI.get_formatted_address_fromKeyLatLnag(query[0], query[1])
        # APIリクエストの制限(1秒/1リクエスト)
        time.sleep(2)
        
        # GoogleMapのPopularTimes取得
        data = livepopulartimes.get_populartimes_by_address(formatted_address)
        #APIレート制限対策
        time.sleep(2)
        
        if 'populartimes' in data:
            for day_data in data['populartimes']:
                if day_data['name'] == "Friday":
                    print(day_data['data'])
                    #18時～21時のデータ
                    dinner_time_popularity[query_tuple] = day_data['data'][18:22]
                    break
        else:
            print(f"混雑データが {formatted_address} で取得できませんでした。")
    
    
    # 出力
    print("金曜日の18時～21時の混雑度:", dinner_time_popularity)
