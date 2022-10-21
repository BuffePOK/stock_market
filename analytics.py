from math import fabs
from copy import copy
from json import load
from os.path import abspath, dirname
from parsing import parsing



def smoothed_moving_average(closes):
    moving_average = []
    length = len(closes)
    sum1 = closes[0]*length
    smma1 = copy(sum1)/length
    moving_average.append(smma1)
    for close in range(len(closes)):
        if close == 0: continue
        sum1 = closes[close]*length
        smma = (sum1 - smma1 + closes[close])/length
        moving_average.append(smma)
        smma1 = copy(smma)
    
    return moving_average
            
def max_min_deviation(values):
    average = sum(values)/len(values)
    deviat = (((average - min(values)) + (max(values) - average)) / 2)
    deviation_values = []
    for value in values:
        deviation_in_value = value - average
        relative_deviation = deviation_in_value / deviat * 100
        deviation_values.append(relative_deviation)

    return deviation_values

def top_buy_sell(values):
    buy = sum(values['buy'])
    sell = sum(values['sell'])
    try:
        difference = (buy/(buy+sell) * 2 - 1) * 100
    except ZeroDivisionError: difference = 0
    
    return difference


def stochastic_oscillator(values):
    minimum = min(values)
    maximum = max(values)
    fast_stochastic = []
    for value in values:
        kt = ((value - minimum)/(maximum - minimum) - 0.5) * 200
        fast_stochastic.append(kt)

    return fast_stochastic[-1]


def commodity_channel_index(high, low, close):
    typical_price_list = []
    for part in range(len(close)):
        typical_price = (high[part] + low[part] + close[part]) / 3
        typical_price_list.append(typical_price)

    sma = sum(typical_price_list)/len(typical_price_list)
    mad = 0
    for part in typical_price_list:
        mad += fabs((part - sma))
    mad = mad / len(typical_price_list)

    cci = (1/0.015) * ((typical_price_list[-1] - sma) / mad)

    
    return cci

def open_interest(closes, depth):
    last_price = closes[-1]
    low_price = last_price * 0.9
    high_price = last_price * 1.1
    sell = 0
    buy = 0
    for bids in depth['bids']:
        if float(bids[0]) > low_price and float(bids[0]) < high_price:
            sell += float(bids[0]) * float(bids[1])
    for asks in depth['bids']:
        if float(asks[0]) > low_price and float(asks[0]) < high_price:
            buy += float(asks[0]) * float(asks[1])

    difference = (buy / (buy + sell) - 0.5) * (-2)

    return difference


def power_players(top): # +
    top_players = top[-1]
    if top_players['longAccount'] > top_players['shortAccount']: chance = float(top_players['longAccount']) * 100
    elif top_players['longAccount'] < top_players['shortAccount']: chance = -float(top_players['shortAccount']) * 100
    else: chance = 0
    return chance


def analyse(coin):
    klines = parsing(coin)
    # parsing_klines = []
    # for kline in klines_wave[0:-2]:
    #     part = {
    #         "open_time":kline[0],
    #         "open":float(kline[1]),
    #         "high":float(kline[2]),
    #         "low":float(kline[3]),
    #         "close":float(kline[4]),
    #         "quote":float(kline[7]),
    #         "number_of_trades":kline[8],
    #         "quote_buy":float(kline[10])
    #     }
    #     parsing_klines.append(part)
    


    closes = []
    minimum = []
    maximum = []
    volumes = []
    opens = []
    for kline in klines:
        closes.append(kline['close'])
        minimum.append(kline['low'])
        maximum.append(kline['high'])
        volumes.append(kline['quote'])
        opens.append(kline['open'])

    moving_average = smoothed_moving_average(closes)


    deviation = max_min_deviation(moving_average)[-1] # super good 9 сделок 2 моржа 1377%
    stochastic = stochastic_oscillator(closes) # super good 9 сделок 3 моржа +1100%
    commodity = commodity_channel_index(maximum, minimum, closes) # супер гуд 12 сделок 3 моржа 1258%
    # buy_sell = top_buy_sell(trades)



    # interests = open_interest(closes, depth)
    # top_players = power_players(top)

    answer = [deviation, stochastic, commodity]


    return answer




def get_chance(coin):
    chances = analyse(coin) # 16

    is_koeff = (sum(chances))/3
    file_path = dirname(abspath(__file__)) + "/koefficients/" + coin + ".json"
    if is_koeff > 0:
        koeffs = load(open(file_path))["koeffs_sell"]
    if is_koeff <= 0:
        koeffs = load(open(file_path))["koeffs_buy"]

    chances = [chances[0]*koeffs[0], chances[1]*koeffs[1], chances[2]*koeffs[2]]

    chance = (sum(chances))/3

    return chance