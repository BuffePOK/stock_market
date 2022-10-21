from math import fabs
from copy import copy
from time import sleep
from parsing import parsing
from os.path import dirname, abspath
from json import load

from stables import crypto_list


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

def relative_strength_index(closes):
    upper = [0]
    down = [0]
    close1 = copy(closes[0])
    for kline in range(len(closes)):
        if 0 == kline: continue
        close = closes[kline]
        if close > close1:
            upper.append(close-close1)
            down.append(0)
        elif close < close1:
            down.append(close1-close)
            upper.append(0)
        elif close == close1:
            down.append(0)
            upper.append(0)
        close1 = copy(close)
    

    MA_upper = smoothed_moving_average(upper)
    MA_down = smoothed_moving_average(down) 

    rsi = []
    for ma in range(len(MA_upper)):
        try:
            rsi_part = 100 * (MA_upper[ma] / (MA_upper[ma] + MA_down[ma]))
        except ZeroDivisionError:
            rsi_part = 100
        rsi.append(rsi_part)
    relative_rsi = max_min_deviation(rsi)

    return relative_rsi[-2], closes[-1]
            
def max_min_deviation(values):
    average = sum(values)/len(values)
    deviat = (((average - min(values)) + (max(values) - average)) / 2)
    deviation_values = []
    for value in values:
        deviation_in_value = value - average
        relative_deviation = deviation_in_value / deviat * 100
        deviation_values.append(relative_deviation)

    return deviation_values

# def top_buy_sell(values):
#     buy = sum(values['buy'])
#     sell = sum(values['sell'])
#     try:
#         difference = (buy/(buy+sell) * 2 - 1) * 100
#     except ZeroDivisionError: difference = 0
    
#     return difference


def stochastic_oscillator(values):
    minimum = min(values)
    maximum = max(values)
    fast_stochastic = []
    for value in values:
        kt = ((value - minimum)/(maximum - minimum) - 0.5) * 200
        fast_stochastic.append(kt)

    return fast_stochastic[-1]

# def directional_movement(low, close, high): # +
#     true_range_list = []
#     close1 = close[0]
#     true_range_list.append((max(high[0], close1) - min(low[0], close1)))

#     for truerange in range(len(close)):
#         if truerange == 0: continue
#         true_range = max(high[truerange], close1) - min(low[truerange], close1)
#         true_range_list.append(true_range)
#         close1 = close[truerange]

#     average_true_range = smoothed_moving_average(true_range_list)


#     Mt_plus_list = []
#     Mt_minus_list = []
#     high1 = high[0]
#     low1 = low[0]
#     Mt_minus_list.append(0)
#     Mt_plus_list.append(0)

#     for Mt in range(len(close)):
#         if Mt == 0: continue
#         Mt_plus = high[Mt] - high1
#         Mt_minus = low[Mt] - low1

#         Mt_plus_list.append(Mt_plus)
#         Mt_minus_list.append(Mt_minus)

#         high1 = high[Mt]
#         low1 = low[Mt]


#     DMt_plus_list = []
#     DMt_minus_list = []

#     DMt_plus_list.append(0)
#     DMt_minus_list.append(0)

#     for DMt in range(len(Mt_minus_list)):
#         if DMt == 0: continue
#         Mt_plus = Mt_plus_list[DMt]
#         Mt_minus = Mt_minus_list[DMt]
#         true_range = average_true_range[DMt]

#         if Mt_plus > Mt_minus and Mt_plus > 0:
#             DMt_plus_list.append((Mt_plus/true_range))
#         elif Mt_plus < Mt_minus or Mt_plus < 0:
#             DMt_plus_list.append(0)
#         else: DMt_plus_list.append(0)

#         if Mt_minus < Mt_plus or Mt_minus < 0:
#             DMt_minus_list.append(0)
#         elif Mt_minus > Mt_plus and Mt_minus > 0:
#             DMt_minus_list.append((Mt_minus/true_range))
#         else: DMt_minus_list.append(0)



#     DIt_plus_list = smoothed_moving_average(DMt_plus_list)
#     DIt_minus_list = smoothed_moving_average(DMt_minus_list)

#     DXIt_list = []
#     for DIt in range(len(DIt_minus_list)):
#         DIt_plus = DIt_plus_list[DIt]
#         DIt_minus = DIt_minus_list[DIt]
#         try:
#             DXIt = 100 * (fabs(DIt_plus - DIt_minus) / (DIt_plus + DIt_minus))
#         except ZeroDivisionError: DXIt = 0
#         DXIt_list.append(DXIt)

#     ADXt_list = smoothed_moving_average(DXIt_list)

#     if (DIt_plus_list[-1] > DIt_minus_list[-1]) and (ADXt_list[-1] > ADXt_list[-2]): chance = -100
#     elif (DIt_plus_list[-1] < DIt_minus_list[-1]) or (ADXt_list[-1] < ADXt_list[-2]): chance = 100
#     else: chance = 0

#     return chance

# def on_balance_volume(closes, volumes):
#     close1 = closes[0]
#     OBVt_list = []
#     OBVt1 = 0
#     OBVt_list.append(0)
#     for OBv in range(len(closes)):
#         close = closes[OBv]
#         volume = volumes[OBv]

#         if close > close1:
#             OBVt = OBVt1 + volume
#         elif close == close1:
#             OBVt = 0
#         elif close < close1:
#             OBVt = OBVt1 - volume

#         OBVt_list.append(OBVt)
#         close1 = close
#         OBVt1 = OBVt

#     OBVt_ma = smoothed_moving_average(OBVt_list)

#     if OBVt_list[-2] < OBVt_ma[-1] and OBVt_list[-1] > OBVt_ma[-1]: chance = -100
#     elif OBVt_list[-2] > OBVt_ma[-1] and OBVt_list[-1] < OBVt_ma[-1]: chance = 100
#     else: chance = 0

#     return chance


def arms_index(opens, closes, volumes):
    advancing_issues = 0
    declining_issues = 0
    advancing_volume = 0
    declining_volume = 0
    for Ai in range(len(closes)):
        opeN = opens[Ai]
        closE = closes[Ai]
        volume = volumes[Ai]
        if opeN > closE: 
            advancing_issues += 1
            advancing_volume += volume
        elif opeN < closE:
            declining_issues += 1
            declining_volume += volume

    
    arm_index = ( ( ( advancing_issues / declining_issues ) / ( advancing_volume / declining_volume ) ) - 0.975 ) * (-800)

    
    return arm_index


def money_flow_index(high, low, closes, volumes):
    typical_price_list = []
    for price in range(len(closes)):
        typical_price = (high[price] + low[price] + closes[price])/3
        typical_price_list.append(typical_price)

    flow_plus = 0
    flow_minus = 0
    for flow in range(len(typical_price_list)):
        try:
            typical_price = typical_price_list[flow]
            typical_price1 = typical_price_list[flow-1]
            volume = volumes[flow]
            if typical_price > typical_price1: flow_plus += volume
            elif typical_price < typical_price1: flow_minus += volume
        except IndexError: continue

    money_refers = flow_plus/flow_minus
    money_flow = (100 - (100/(1 + money_refers)) - 50) * 2


    return money_flow


# def accumulation_distribution_index(high, low, close, volume):
#     accdict_list = []
#     try:
#         clv1 = ( ( ( close[0] - low[0] ) - ( high[0] - close[0] ) ) / ( high[0] - low[0] ) ) * volume[0]
#     except ZeroDivisionError: clv1 = 0
#     accdict1 = copy(clv1)
#     accdict_list.append(accdict1)

#     for part in range(len(close)):
#         try:
#             clv = ( ( ( close[part] - low[part] ) - ( high[part] - close[part] ) ) / ( high[part] - low[part] ) ) * volume[part]
#         except ZeroDivisionError: clv = 0
#         accdict = accdict1 + clv
#         accdict_list.append(accdict)
#         accdict1 = copy(accdict)

#     accdict_list_average = smoothed_moving_average(accdict_list)
#     if accdict_list[-2] < accdict_list_average[-1] and accdict_list[-1] > accdict_list_average[-1]: chance = -100
#     elif accdict_list[-2] > accdict_list_average[-1] and accdict_list[-1] < accdict_list_average[-1]: chance = 100
#     else: chance = 0
#     return chance


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


# def ease_of_movement_value(high, low, volumes):
#     high1 = high[0]
#     low1 = low[0]
#     EMVt_list = []
#     for part in range(len(volumes)):
#         if part == 0: continue
#         try:
#             EMVt = ( ( ( high[part] + low[part] ) / 2 ) - ( ( high1 + low1 ) / 2 ) ) / ( volumes[part] / ( high[part] - low[part] ) )
#         except ZeroDivisionError: EMVt = 0
#         EMVt_list.append(EMVt)
#         high1 = copy(high[part])
#         low1 = copy(low[part])

#     EMVt_list = EMVt_list[-384:]
#     EMVt_average = smoothed_moving_average(EMVt_list)

#     if EMVt_average[-1] > 0 and EMVt_average[-2] < 0: chance = -100
#     elif EMVt_average[-1] < 0 and EMVt_average[-2] > 0: chance = 100
#     else: chance = 0

#     return chance


# def advance_decline_line(opens, closes):
#     if opens[0] < closes[0]: ADLt1 = 1
#     elif opens[0] > closes[0]: ADLt1 = -1
#     elif opens[0] == closes[0]: ADLt1 = 0
    
#     ADLt_list = []
#     for part in range(len(closes)):
#         if part == 0: continue

#         if closes[part] > opens[part]: ADLt = ADLt1 + 1
#         elif closes[part < opens[part]]: ADLt = ADLt1 - 1
#         elif closes[part] == opens[part]: ADLt = ADLt1
#         ADLt_list.append(ADLt)
#         ADLt1 = copy(ADLt)

#     if ADLt_list[-1] > ADLt_list[-2]: chance = 100
#     elif ADLt_list[-1] < ADLt_list[-2]: chance = -100
#     elif ADLt_list[-1] == ADLt_list[-2]: chance = 0

#     return chance

# def rate_of_change(closes):
#     momentum1 = closes[-1] - closes[-13]
#     momentum2 = closes[-2] - closes[-14]
#     if momentum1 > 0 and momentum2 < 0: chance = -100
#     elif momentum1 < 0 and momentum2 > 0: chance = 100
#     else: chance = 0

#     return chance


# def price_volume_trend(closes, volumes):
#     PVTt1 = 0
#     close1 = closes[0]
#     PVTt_list = []
#     for part in range(len(closes)):
#         PVTt = PVTt1 + volumes[part] * ((closes[part] - close1)/close1)
#         PVTt_list.append(PVTt)
#         PVTt1 = copy(PVTt)
#         close1 = copy(closes[part])
#     PVTt_average = smoothed_moving_average(PVTt_list)
#     if PVTt_list[-2] < PVTt_average[-1] and PVTt_list[-1] > PVTt_average[-1]: return -100
#     elif PVTt_list[-2] > PVTt_average[-1] and PVTt_list[-1] < PVTt_average[-1]: return 100
#     else: return 0


# def open_interest(closes, depth):
#     last_price = closes[-1]
#     low_price = last_price * 0.9
#     high_price = last_price * 1.1
#     sell = 0
#     buy = 0
#     for bids in depth['bids']:
#         if float(bids[0]) > low_price and float(bids[0]) < high_price:
#             sell += float(bids[0]) * float(bids[1])
#     for asks in depth['bids']:
#         if float(asks[0]) > low_price and float(asks[0]) < high_price:
#             buy += float(asks[0]) * float(asks[1])

#     difference = (buy / (buy + sell) - 0.5) * (-2)

#     return difference


# def power_players(top): # +
#     top_players = top[-1]
#     if top_players['longAccount'] > top_players['shortAccount']: chance = float(top_players['longAccount']) * 100
#     elif top_players['longAccount'] < top_players['shortAccount']: chance = -float(top_players['shortAccount']) * 100
#     else: chance = 0
#     return chance

def support_price(depth):
    bids = [[0,0]]
    asks = [[0,0]]
    for ans in depth["bids"]:
        money = float(ans[0])*float(ans[1])
        ans.append(money)
        last_max = float(bids[-1][0])*float(bids[-1][1])

        if money >= last_max:
            bids.append(ans)

    for ans in depth["asks"]:
        money = float(ans[0])*float(ans[1])
        ans.append(money)
        last_max = float(asks[-1][0])*float(asks[-1][1])

        if money >= last_max:
            asks.append(ans)

    bids = bids[-3:]
    asks = asks[-3:]
    # bids.reverse()
    # asks.reverse()
    return "Bids: ", bids, "Asks: ", asks



def analyse(coin):
    klines, depth = parsing(coin)
    price_line = support_price(depth)
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

    # moving_average = smoothed_moving_average(closes)


    rsi = relative_strength_index(closes)
    # deviation = max_min_deviation(moving_average)[-1]
    # buy_sell = top_buy_sell(trades)
    # stochastic = stochastic_oscillator(closes)
    # directional_movement_index = directional_movement(minimum, closes, maximum)
    # volume = on_balance_volume(closes, volumes)
    # arm_index = arms_index(opens, closes, volumes)
    # money_flow = money_flow_index(maximum, minimum, closes, volumes)
    # accumulation_index = accumulation_distribution_index(maximum, minimum, closes, volumes)
    # commodity = commodity_channel_index(maximum, minimum, closes)
    # movement = ease_of_movement_value(maximum, minimum, volumes)
    # decline_line = advance_decline_line(opens, closes)
    # change = rate_of_change(closes)
    # price_volume = price_volume_trend(closes, volumes)
    # interests = open_interest(closes, depth)
    # top_players = power_players(top)
    price_line = support_price(depth)

    return rsi, price_line




def get_chance(coin):
    chances = analyse(coin) # 16
    denominator = 6

    is_koeff = (sum(chances)) / denominator
    file_path = dirname(abspath(__file__)) + "/koefficients/" + coin + ".json"
    if is_koeff > 0:
        koeffs = load(open(file_path))["koeffs_sell"]
    if is_koeff <= 0:
        koeffs = load(open(file_path))["koeffs_sell"]

    chances = [chances[0]*koeffs[0], chances[1]*koeffs[1], chances[2]*koeffs[2], chances[3]*koeffs[3], 
    chances[4]*koeffs[4], chances[5]*koeffs[5]]

    chance = (sum(chances)) / denominator

    return chance



if __name__ == "__main__":
    for coin in crypto_list:
        answer = analyse(coin)
        sleep(1)
        # if answer[0][0] > 90 or answer[0][0] < -90:
        print(coin, answer)
        