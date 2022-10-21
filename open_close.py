from json import load, dump
from analytics import get_chance
from time import sleep, time
from parsing import parsing
from stables import stable_binance, crypto_list, trading_ratio
from keys import keys
from requests import get
from binance.client import Client
from os.path import dirname, abspath


def open_position(coin, client):

    file_path = dirname(abspath(__file__)) + "/open.json"
    file_json = open(file_path)
    open_json = load(file_json)

    file_json.close()

    for index in range(len(open_json["open"])):
        if open_json["open"][index]["coin"] == coin:
            if open_json["open"][index]["margin_call"] >= (time()-3600): return -1

            elif open_json["open"][index]["margin_call"] <= (time()-3600) and open_json["open"][index]["margin_call"] != 0: 
                del open_json["open"][index]
                file_json = open(file_path, "w")
                dump(open_json, file_json, sort_keys=True, indent=2)
                break

            close_position(open_json["open"][index], client)
            return 100

    # if len(open_json["open"]) > 13: return -1

    chance = get_chance(coin)

    if chance >= 50:
        url = stable_binance["base"] + stable_binance["price"]
        price = float(get(url, params={"symbol":coin}).json()["price"])
        if price > 2000: quantity = round((25/price), 3) # Измените число, чтобы изменить ставку
        elif price >= 500 and price <= 2000: quantity = round((25/price), 2) # Измените число, чтобы изменить ставку
        elif price <= 500 and price >= 50: quantity = round((25/price), 1) # Измените число, чтобы изменить ставку
        else: quantity = round((25/price), 0) # Измените число, чтобы изменить ставку

        client.futures_create_order(
            symbol=coin,
            side="SELL",
            quantity=quantity,
            type="MARKET",
            timestamp=(time()*1000)
        )

        margin_call = 1.0886*price
        to_json = {
            "coin":coin,
            "side":"SELL",
            "open_price":price,
            "open_chance":chance,
            "margin_call":0,
            "quantity":quantity,
            "open_time":time()*1000,
            "margin_call_price":margin_call,
            "profit": 0
        }
        print(to_json)

        open_json["open"].append(to_json)
        
        file_json = open(file_path, 'w')
        dump(open_json, file_json, sort_keys=True, indent=2)
        file_json.close()

        return 200




    if chance <= -50:
        url = stable_binance["base"] + stable_binance["price"]
        price = float(get(url, params={"symbol":coin}).json()["price"])
        if price > 2000: quantity = round((25/price), 3) # Измените число, чтобы изменить ставку
        elif price >= 500 and price <= 2000: quantity = round((25/price), 2) # Измените число, чтобы изменить ставку
        elif price <= 500 and price >= 50: quantity = round((25/price), 1) # Измените число, чтобы изменить ставку
        else: quantity = round((25/price), 0) # Измените число, чтобы изменить ставку

        client.futures_create_order(
            symbol=coin,
            side="BUY",
            quantity=quantity,
            type="MARKET",
            timestamp=(time()*1000)
        )

        margin_call = price / 1.10054
        to_json = {
            "coin":coin,
            "side":"BUY",
            "open_price":price,
            "open_chance":chance,
            "margin_call":0,
            "quantity":quantity,
            "open_time":time()*1000,
            "margin_call_price":margin_call,
            "profit": 0
        }
        print(to_json)

        open_json["open"].append(to_json)

        file_json = open(file_path, "w")
        dump(open_json, file_json, sort_keys=True, indent=2)
        file_json.close()


        return 200

















def close_position(from_open_json, client):
    file_path = dirname(abspath(__file__)) + "/open.json"
    kline = parsing(from_open_json["coin"])
    for kl in kline:
            if (from_open_json["side"] == "SELL" and kl["open_time"] > from_open_json["open_time"] and float(kl["high"]) >= from_open_json["margin_call_price"]) or (from_open_json["side"] == "BUY" and kl["open_time"] > from_open_json["open_time"] and float(kl["low"]) <= from_open_json["margin_call_price"]):
                file_path = dirname(abspath(__file__)) + "/open.json"


                profit_path = dirname(abspath(__file__)) + "/profit/" + from_open_json["coin"] + ".json"
                profit_json = load(open(profit_path))

                file_json = open(file_path)
                open_json = load(file_json)
                file_json.close()

                from_open_json["margin_call"] = time()
                from_open_json["profit"] = -100

                profit_json["profit"].append(from_open_json)


                profit_write = open(profit_path, "w")
                dump(profit_json, profit_write, sort_keys=True, indent=2)


                for index in range(len(open_json["open"])):
                    if open_json["open"][index]["coin"] == from_open_json["coin"]:
                        open_json["open"][index] = from_open_json
                        
                        file_json = open(file_path, 'w')
                        dump(open_json, file_json, sort_keys=True, indent=2)
                        file_json.close()

                        file = open(str(dirname(abspath(__file__)) + "/profit.txt"), 'a')
                        file.write(str(from_open_json["coin"] + ": Profit: -100. Start price: " + str(from_open_json["open_price"]) + ". Close price: " + str(kl["close"]) + ". side: " + from_open_json["side"] + "\n"))
                        return -1




    profit = get_chance(from_open_json["coin"])

    if from_open_json["side"] == "SELL" and profit <= 7.0:
        client.futures_create_order(
            symbol=from_open_json["coin"],
            side="BUY",
            quantity=from_open_json["quantity"],
            type="MARKET",
            timestamp=(time()*1000)
        )

        end_price = float(get(url="https://fapi.binance.com/fapi/v1/ticker/price", params={"symbol":from_open_json["coin"]}).json()["price"])
        profit = ((from_open_json["open_price"]/end_price) - 1) * trading_ratio[from_open_json["coin"]] * 100


        profit_path = dirname(abspath(__file__)) + "/profit/" + from_open_json["coin"] + ".json"
        profit_json = load(open(profit_path))

        file_json = open(file_path)
        open_json = load(file_json)
        file_json.close()

        for index in range(len(open_json["open"])):
            if open_json["open"][index]["coin"] == from_open_json["coin"]:
                open_json["open"][index]["profit"] = profit
                profit_json["profit"].append(open_json["open"][index])

                del open_json["open"][index]
                file_json = open(file_path, "w")
                dump(open_json, file_json, sort_keys=True, indent=2)
                break
        
        profit_write = open(profit_path, "w")
        dump(profit_json, profit_write, sort_keys=True, indent=2)


        
        file = open(str(dirname(abspath(__file__)) + "/profit.txt"), 'a')
        file.write(str(from_open_json["coin"] + ": Profit: " + str(profit) + " Start price: " + str(from_open_json["open_price"]) + ". Close price: " + str(end_price) + "\n"))

        return 200


    if from_open_json["side"] == "BUY" and profit >= -7.0:
        client.futures_create_order(
            symbol=from_open_json["coin"],
            side="SELL",
            quantity=from_open_json["quantity"],
            type="MARKET",
            timestamp=(time()*1000)
        )

        file_json = open(file_path)
        open_json = load(file_json)
        file_json.close()

        end_price = float(get(url="https://fapi.binance.com/fapi/v1/ticker/price", params={"symbol":from_open_json["coin"]}).json()["price"])
        profit = ((end_price/from_open_json["open_price"]) - 1) * trading_ratio[from_open_json["coin"]] * 100

        profit_path = dirname(abspath(__file__)) + "/profit/" + from_open_json["coin"] + ".json"
        profit_json = load(open(profit_path))

        file_json = open(file_path)
        open_json = load(file_json)
        file_json.close()

        for index in range(len(open_json["open"])):
            if open_json["open"][index]["coin"] == from_open_json["coin"]:
                open_json["open"][index]["profit"] = profit
                profit_json["profit"].append(open_json["open"][index])

                del open_json["open"][index]
                file_json = open(file_path, "w")
                dump(open_json, file_json, sort_keys=True, indent=2)
                break

        profit_write = open(profit_path, "w")
        dump(profit_json, profit_write, sort_keys=True, indent=2)

        
        file = open(str(dirname(abspath(__file__)) + "/profit.txt"), 'a')
        file.write(str(from_open_json["coin"] + ": Profit: " + str(profit) + " Start price: " + str(from_open_json["open_price"]) + ". Close price: " + str(end_price) + "\n"))

        return 200
    return 100


def main():
    client = Client(api_key=keys["api_key"], api_secret=keys["secret_key"])
    while True:
        accum = 1
        for coin in crypto_list:
            print(accum, coin)
            open_position(coin, client)
            sleep(3)
            accum += 1


if __name__ == "__main__":

    main()


# 0