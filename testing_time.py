# from copy import copy
# from time import time 
import json
# from requests import get
# from time import sleep
# from random import randint
# from stables import crypto
# from multiprocessing import Process
# from os.path import abspath, dirname
from stables import crypto_list





# total_money = 0
# money = 5
# for i in range(100):
#     total_money += 5*1.18
# for i in range(100):
#     total_money += 20*1.18
# for i in range(100):
#     total_money += 100*1.18
# for i in range(100):
#     total_money += 500*1.18
# for i in range(100):
#     total_money += 1000*1.18
# for i in range(100):
#     total_money += 2000*1.18
# for i in range(100):
#     total_money += 5000*1.18
# for i in range(100):
#     total_money += 10000*1.18
# for i in range(100):
#     total_money += 20000*1.18
# for i in range(100):
#     total_money += 25000*1.18
# print(total_money)










# profit_str = ""
# total_profit = 0
# amount_of_deals = 0
# margin_calls = 0

# for coin in crypto_list:
#     file_path = abspath(dirname(__file__)) + "/profit/" + coin + ".json"
#     file = json.load(open(file_path))


#     profit = 0
#     margin = 0
#     deals = 0
#     for answer in file["buyers"]:
#         if answer["chance_buy"] >= -50.0: continue
#         profit += answer["profit"]
#         if answer["profit"] == -100: margin += 1
#         deals += 1
#         if answer["chance_sell"] <= 50.0: continue
#         profit += answer["profit"]
#         if answer["profit"] == -100: margin += 1
#         deals += 1


#     amount_of_deals += deals
#     total_profit += profit
#     margin_calls += margin
#     profit_str += coin + ": " + str(profit) + " || Margin calls: " + str(margin) + " || Amount of deals: " + str(deals) + "\n"

# profit_str += "===============\n" + "Total profit: " + str(total_profit) + "\n" + "Amount of deals: " + str(amount_of_deals) + "\n" + " Margin calls: " + str(margin_calls) + "\n"

# file = open(str(abspath(dirname(__file__)) + "/profit.txt"), "w")
# file.write(profit_str)
# file.close()











# def klines(coin, url):
#     file_path = "klines/klines_" + coin + ".json"
#     try:
#         klines_json = json.load(open(file_path))
#     except FileNotFoundError:
#         file = open(file_path, "w")
#         json.dump({}, file)
#         file.close()
#         klines(coin, url)

#     klines_json = json.load(open(file_path))



#     param0 = {
#                 "symbol":coin,
#                 "interval":"15m",
#                 "limit":1500
#             }
#     answer0 = get(url, params=param0).json()
#     param1 = {
#                 "symbol":coin,
#                 "interval":"15m",
#                 "limit":1500,
#                 "endTime":answer0[0][0]-1
#     }
#     answer1 = get(url, params=param1).json()
#     param2 = {
#                 "symbol":coin,
#                 "interval":"15m",
#                 "limit":1500,
#                 "endTime":answer1[0][0]-1
#     }
#     answer2 = get(url, params=param2).json()
#     param3 = {
#                 "symbol":coin,
#                 "interval":"15m",
#                 "limit":1500,
#                 "endTime":answer2[0][0]-1
#     }
#     answer3 = get(url, params=param3).json()
#     param4 = {
#                 "symbol":coin,
#                 "interval":"15m",
#                 "limit":1500,
#                 "endTime":answer3[0][0]-1
#     }
#     answer4 = get(url, params=param4).json()
#     param5 = {
#                 "symbol":coin,
#                 "interval":"15m",
#                 "limit":1500,
#                 "endTime":answer4[0][0]-1
#     }
#     answer5 = get(url, params=param5).json()
#     param6 = {
#                 "symbol":coin,
#                 "interval":"15m",
#                 "limit":1500,
#                 "endTime":answer5[0][0]-1
#     }
#     answer6 = get(url, params=param6).json()
#     param7 = {
#                 "symbol":coin,
#                 "interval":"15m",
#                 "limit":1500,
#                 "endTime":answer6[0][0]-1
#     }
#     answer7 = get(url, params=param7).json()
#     param8 = {
#                 "symbol":coin,
#                 "interval":"15m",
#                 "limit":1500,
#                 "endTime":answer7[0][0]-1
#     }
#     answer8 = get(url, params=param8).json()
#     answer = answer8 + answer7 + answer6 + answer5 + answer4 + answer3 + answer2 + answer1 + answer0
#     # 



#     klines_json[coin] = []
#     for kline in answer:
#         klines_json[coin].append(kline)
    
#     file = open(file_path, "w")
#     json.dump(klines_json, file, sort_keys=True, indent=2)
#     file.close()

# for coin in crypto_list:
#     # Process(target = klines, args=(coin, "https://fapi.binance.com/fapi/v1/klines"))
#     print(coin)
#     klines(coin, "https://fapi.binance.com/fapi/v1/klines")
#     # sleep(1)


























# for coin in crypto_list:
#     file_path = "koefficients/" + coin + ".json"
#     file = open(file_path, "w")

#     to_file = {
#         "koeffs_buy":[1,1,1,1],
#         "koeffs_sell":[1,1,1,1]
#     }

#     json.dump(to_file, file, sort_keys=True, indent=2)
#     file.close()










for coin in crypto_list:
    file_path = "profit/" + coin + ".json"
    file = open(file_path, "w")

    to_file = {
        "profit":[]
#   "buyers": [
#     {
#       "chance_buy": 0,
#       "chance_sell": 0,
#       "chances_buy": [],
#       "chances_sell": [],
#       "coin": "coin",
#       "end_price": 0,
#       "koeffs": [],
#       "margin_call": 0,
#       "profit": 0,
#       "start_price": 0,
#       "time": 0,
#       "trading_ratio": 0
#     }
#   ]
#   "sellers": [
#     {
#       "chance_buy": 0,
#       "chance_sell": 0,
#       "chances_buy": [],
#       "chances_sell": [],
#       "coin": "coin",
#       "end_price": 0,
#       "koeffs": [],
#       "margin_call": 0,
#       "profit": 0,
#       "start_price": 0,
#       "time": 0,
#       "trading_ratio": 0
#     }
#   ]
}

    json.dump(to_file, file, sort_keys=True, indent=2)
    file.close()