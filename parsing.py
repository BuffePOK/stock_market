from stables import stable_binance
from requests import get

def depth(coin, url):
    param = {
                "symbol":coin,
                "limit":1000
            }
    order_book = get(url, params=param).json()
    return order_book

# def trades(coin, url):
#     param = {
#                 "symbol":coin,
#                 "limit":1000
#             }
#     answer = get(url, params=param).json()

#     sell = []
#     buy = []
#     sum_buy = 0.0
#     sum_sell = 0.0
#     for data in answer:
#         if data["isBuyerMaker"] == True:
#             sum_buy += float(data["quoteQty"])
#             if float(data["quoteQty"]) > 5000.0:
#                 buy.append(float(data["quoteQty"]))
#         elif data["isBuyerMaker"] == False:
#             sum_sell += float(data["quoteQty"])
#             if float(data["quoteQty"]) > 5000.0:
#                 sell.append(float(data["quoteQty"]))

#             trades_list = {}
#             trades_list["buy"] = sorted(buy)
#             trades_list["sell"] = sorted(sell)
#             trades_list["sum_buy"] = sum_buy
#             trades_list["sum_sell"] = sum_sell

#     return trades_list

def klines(coin, url):
    param = {
                "symbol":coin,
                "interval":"15m",
                "limit":1344
            }
    answer = get(url, params=param).json()
    parsing_klines = []
    for kline in answer:
        part = {
            "open_time":kline[0],
            "open":float(kline[1]),
            "high":float(kline[2]),
            "low":float(kline[3]),
            "close":float(kline[4]),
            "quote":float(kline[7]),
            "number_of_trades":kline[8],
            "quote_buy":float(kline[10])
        }
        parsing_klines.append(part)
    return parsing_klines

# def top_long_short_positions(coin, url):
#     param = {
#                 "symbol":coin,
#                 "period":"15m",
#                 "limit":300
#             }
#     top_positions = get(url, params=param).json()
#     return top_positions

def parsing(coin):
    depth_result = depth(url=stable_binance['base']+stable_binance['order_book'], coin=coin)
    # trades_result = trades(url=stable_binance['base']+stable_binance['trades_list'], coin=coin)
    klines_result = klines(url=stable_binance['base']+stable_binance['klines'], coin=coin)
    # top_result = top_long_short_positions(url=stable_binance['base']+stable_binance['top_long_short_positions'], coin=coin)
    return klines_result, depth_result


# if __name__ == "__main__":
#     main()