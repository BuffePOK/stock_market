# from copy import copy
from time import time
import json
from requests import get
from time import sleep
# from random import randint
# from stables import crypto
# from multiprocessing import Process
from os.path import abspath, dirname
from stables import crypto_list
from binance.client import Client


# client = Client(api_key=keys["api_key"], api_secret=keys["secret_key"])
# for coin in crypto_list:
#     try:
#         print(coin)
#         leverage = client.futures_change_margin_type(symbol = coin, marginType="ISOLATED", timestamp = time()*1000)
#     except: print(coin, "except")




# profit_str = ""
# total_profit = 0
# amount_of_deals = 0
# margin_calls = 0

# for coin in crypto_list:
#     file_path = abspath(dirname(__file__)) + "/profit/" + coin + ".json"
#     file = json.load(open(file_path))


#     profit = 0
#     margin = 0
#     deals = -2
#     for answer in file["buyers"]:
#         profit += answer["profit"]
#         if answer["profit"] == -100: margin += 1
#         deals += 1
#     for answer in file["sellers"]:
#         profit += answer["profit"]
#         if answer["profit"] == -100: margin += 1
#         deals += 1





#     amount_of_deals += deals
#     total_profit += profit
#     margin_calls += margin
#     profit_str += coin + ": " + str(profit) + " || Margin calls: " + str(margin) + " || Amount of deals: " + str(deals) + "\n"

# profit_str += "===============\n" + "Total profit: " + str(total_profit) + "\n" + "Amount of deals: " + str(amount_of_deals) + "\n" + " Margin calls: " + str(margin_calls) + "\n"

# file = open(str(abspath(dirname(__file__)) + "/profit_procent.txt"), "w")
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

#     answer = []
    
#     try:
#         param0 = {
#                     "symbol":coin,
#                     "interval":"15m",
#                     "limit":1500
#                 }
#         answer0 = get(url, params=param0).json()
#         answer += answer0
#     except: 
#         print(coin, "0")
#         aaa = input()


#     try:
#         for i in range(2):
#             param0 = {
#                         "symbol":coin,
#                         "interval":"15m",
#                         "limit":1500,
#                         "endTime":answer0[0][0]-1
#                     }
#             answer0 = get(url, params=param0).json()
#             answer += answer0
#     except: 
#         print(coin, i)
#         # aaa = input()

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

#     answer = []
    
#     try:
#         param0 = {
#                     "symbol":coin,
#                     "interval":"15m",
#                     "limit":1500
#                 }
#         answer0 = get(url, params=param0).json()
#         answer += answer0
#     except: 
#         print(coin, "0")
#         aaa = input()


#     try:
#         param1 = {
#                     "symbol":coin,
#                     "interval":"15m",
#                     "limit":1500,
#                     "endTime":answer0[0][0]-1
#         }
#         answer1 = get(url, params=param1).json()
#         answer += answer1
#     except: 
#         print(coin, "1")
#         aaa = input()


#     try:
#         param2 = {
#                     "symbol":coin,
#                     "interval":"15m",
#                     "limit":1500,
#                     "endTime":answer1[0][0]-1
#         }
#         answer2 = get(url, params=param2).json()
#         answer += answer2
#     except: 
#         print(coin, "2")
#         aaa = input()


#     try:
#         param3 = {
#                     "symbol":coin,
#                     "interval":"15m",
#                     "limit":1500,
#                     "endTime":answer2[0][0]-1
#         }
#         answer3 = get(url, params=param3).json()
#         answer += answer3
#     except: 
#         print(coin, "3")
#         aaa = input()


#     try:
#         param4 = {
#                     "symbol":coin,
#                     "interval":"15m",
#                     "limit":1500,
#                     "endTime":answer3[0][0]-1
#         }
#         answer4 = get(url, params=param4).json()
#         answer += answer4
#     except: 
#         print(coin, "4")
#         aaa = input()



#     try:
#         param5 = {
#                     "symbol":coin,
#                     "interval":"15m",
#                     "limit":1500,
#                     "endTime":answer4[0][0]-1
#         }
#         answer5 = get(url, params=param5).json()
#         answer += answer5
#     except: 
#         print(coin, "5")
#         aaa = input()


#     try:
#         param6 = {
#                     "symbol":coin,
#                     "interval":"15m",
#                     "limit":1500,
#                     "endTime":answer5[0][0]-1
#         }
#         answer6 = get(url, params=param6).json()
#         answer += answer6
#     except: 
#         print(coin, "6")
#         aaa = input()


#     try:
#         param7 = {
#                     "symbol":coin,
#                     "interval":"15m",
#                     "limit":1500,
#                     "endTime":answer6[0][0]-1
#         }
#         answer7 = get(url, params=param7).json()
#         answer += answer7
#     except: 
#         print(coin, "7")
#         aaa = input()


#     try:
#         param8 = {
#                     "symbol":coin,
#                     "interval":"15m",
#                     "limit":1500,
#                     "endTime":answer7[0][0]-1
#         }
#         answer8 = get(url, params=param8).json()
#         answer += answer8
#     except: 
#         print(coin, "8")
#         aaa = input()



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
#     sleep(1)
























# print("koeffs zero")

# for coin in crypto_list:
#     file_path = "koefficients/" + coin + ".json"
#     file = open(file_path, "w")

#     to_file = {
#         "koeffs_buy":[1,1,1,1,1,1],
#         "koeffs_sell":[1,1,1,1,1,1]
#     }

#     json.dump(to_file, file, sort_keys=True, indent=2)
#     file.close()








# print("profit zero")

# for coin in crypto_list:
#     file_path = "profit/" + coin + ".json"
#     file = open(file_path, "w")

#     to_file = {
#   "profit": [
#   ]
# }

#     json.dump(to_file, file, sort_keys=True, indent=2)
#     file.close()



