# crypto_list = [ "BCHUSDT", 'BTCUSDT', 
# 'EOSUSDT', 'ETCUSDT', 'ETHUSDT', 'LTCUSDT', 'XRPUSDT']

crypto_list = [ 
                 "BTCUSDT", "ETHUSDT", "UNFIUSDT", "SOLUSDT", "GMTUSDT", "MATICUSDT",
                 "SRMUSDT", "DYDXUSDT", "AVAXUSDT", "ADAUSDT", "NEARUSDT",
                 "SANDUSDT", "XRPUSDT", "DOTUSDT", "APEUSDT", "AAVEUSDT", "OGNUSDT",
                 "DOGEUSDT", "UNIUSDT", "LINKUSDT", "FTMUSDT", "AXSUSDT", "CRVUSDT", "ONEUSDT",
                 "WAVESUSDT", "LTCUSDT", "ATOMUSDT", "RUNEUSDT", "TRXUSDT", "GALAUSDT", "STORJUSDT",
                 "COMPUSDT", "BCHUSDT", "MANAUSDT", "BAKEUSDT", "RLCUSDT",
                 "ETCUSDT", "ONTUSDT", "FILUSDT", "XTZUSDT", "FLMUSDT", "1INCHUSDT",
                 "EOSUSDT", "GRTUSDT", "ZILUSDT", "LITUSDT", "PEOPLEUSDT", "BELUSDT", "RSRUSDT",
                 "SUSHIUSDT", "OPUSDT", "THETAUSDT", "SNXUSDT", "XMRUSDT", "ALGOUSDT",
                 "GTCUSDT", "ZRXUSDT", "EGLDUSDT", "KAVAUSDT", "JASMYUSDT", "ZECUSDT",
                 "VETUSDT", "BATUSDT", "ALICEUSDT", "RAYUSDT", "BANDUSDT", "RENUSDT", "XLMUSDT",
                 "MTLUSDT", "QTUMUSDT", "ENJUSDT", "YFIUSDT", "NEOUSDT", "GALUSDT", "ARPAUSDT",
                 "ENSUSDT", "CELRUSDT", "ATAUSDT", "SKLUSDT", "KNCUSDT", "IOTXUSDT",
                 "ARUSDT", "API3USDT", "CHZUSDT", "XEMUSDT", "BLZUSDT", "ROSEUSDT",
                 "AUDIOUSDT", "C98USDT", "WOOUSDT", "IMXUSDT", "OCEANUSDT",
                 "LRCUSDT", "HBARUSDT", "DENTUSDT", "CTKUSDT", "MKRUSDT", "DASHUSDT", "IOSTUSDT",
                 "CTSIUSDT", "BNXUSDT", "ZENUSDT", "SXPUSDT", "CHRUSDT", "HNTUSDT",
                 "OMGUSDT", "MASKUSDT", "LINAUSDT", "STMXUSDT", "ANTUSDT", "KSMUSDT",
                 "CELOUSDT", "ALPHAUSDT", "FTTUSDT", "FLOWUSDT", "COTIUSDT", "HOTUSDT"
]

stable_binance = {
"base":"https://fapi.binance.com",

# https://binance-docs.github.io/apidocs/futures/en/#market-data-endpoints
"ping":"/fapi/v1/ping", # пропинговка. Ответ: 100
"server_time":"/fapi/v1/time", # Время на сервере (Восточноевропейское)
"exchange_info":"/fapi/v1/exchangeInfo", # Текущие правила биржевой торговли и информация о символах (-)
"order_book":"/fapi/v1/depth", # Глубина (открытые позиции на покупку/продажу на определенной цене) (+)
"trades_list":"/fapi/v1/trades", # Последние рыночные сделки (Только рыночные, не ADL) (+)
"old_trades_list":"/fapi/v1/historicalTrades", # старые рыночные сделки (Только рыночные, не ADL) (+)
"compressed_trades_list":"/fapi/v1/aggTrades", # сжатые рыночные сделки (+)
"klines":"/fapi/v1/klines", # свечи (+)
"contract_klines":"/fapi/v1/continuousKlines", # свечи для контрактов (+)
"index_klines":"/fapi/v1/indexPriceKlines", # свечи для индексной цены (-)
"mark_klines":"/fapi/v1/markPriceKlines", # свечи для цены маркировки (+)
"mark_price":"/fapi/v1/premiumIndex", # Цена наценки и Ставка финансирования (-)
"funding_rate_history":"/fapi/v1/fundingRate", # История Ставок Финансирования (-)
"price_change_24h":"/fapi/v1/ticker/24hr", # изменения цен в течение 24-часов (+)
"price":"/fapi/v1/ticker/price", # Последняя цена (+)
"book_ticker":"/fapi/v1/ticker/bookTicker", # Лучшая цена/количество в книге заказов (-)
"open_interest":"/fapi/v1/openInterest", # настоящий открытый интерес (-)
"open_interest_statistics":"/futures/data/openInterestHist", # история открытого интереса (-)
"top_long_short_accounts":"/futures/data/topLongShortAccountRatio", # соотношение лонг/шорт топ аккаунтов (-)
"top_long_short_positions":"/futures/data/topLongShortPositionRatio", # соотношение лонг/шорт топ позиций (+)
"long_short_ratio":"/futures/data/globalLongShortAccountRatio", # соотношение лонг/шорт (-)
"taker_buy_sell_volume":"/futures/data/takerlongshortRatio", # соотношение лонг/шорт тейкеров (-)
"BLVT_NAV_kline":"/fapi/v1/lvtKlines", # хз (??)
"index_info":"/fapi/v1/indexInfo", # информация о паре составного индекса (??)
"asset_index":"/fapi/v1/assetIndex" # Индекс активов в мульти-режиме (??)
}

trading_ratio = {
                 "BTCUSDT": 10, "ETHUSDT": 10, "BTCBUSD": 10, "UNFIUSDT": 10, "SOLUSDT": 10, "ETHBUSD": 10, "GMTUSDT": 10, "MATICUSDT": 10,
                 "SRMUSDT": 10, "DYDXUSDT": 10, "100SHIBUSDT": 10, "AVAXUSDT": 10, "ADAUSDT": 10, "BNBUSDT": 10, "NEARUSDT": 10,
                 "SANDUSDT": 10, "XRPUSDT": 10, "DOTUSDT": 10, "APEUSDT": 10, "AAVEUSDT": 10, "OGNUSDT": 10, "TRBUSDT": 10, "SOLBUSD": 10,
                 "DOGEUSDT": 10, "UNIUSDT": 10, "LINKUSDT": 10, "FTMUSDT": 10, "AXSUSDT": 10, "CRVUSDT": 10, "ONEUSDT": 10,
                 "GALABUSD": 10, "WAVESUSDT": 10, "LTCUSDT": 10, "ATOMUSDT": 10, "RUNEUSDT": 10, "TRXUSDT": 10, "GALAUSDT": 10, "STORJUSDT": 10,
                 "COMPUSDT": 10, "BCHUSDT": 10, "MANAUSDT": 10, "BAKEUSDT": 10, "RLCUSDT": 10, "LUNA2BUSD": 10, "100LUNCBUSD": 10,
                 "ICPBUSD": 10, "ETCUSDT": 10, "ONTUSDT": 10, "FILUSDT": 10, "XTZUSDT": 10, "FLMUSDT": 10, "GMTBUSD": 10, "1INCHUSDT": 10,
                 "BNBBUSD": 10, "EOSUSDT": 10, "GRTUSDT": 10, "ZILUSDT": 10, "LITUSDT": 10, "PEOPLEUSDT": 10, "BELUSDT": 10, "RSRUSDT": 10,
                 "SUSHIUSDT": 10, "OPUSDT": 10, "THETAUSDT": 10, "SNXUSDT": 10, "XMRUSDT": 10, "ALGOUSDT": 10,
                 "GTCUSDT": 10, "ZRXUSDT": 10, "ANCBUSD": 10, "ADABUSD": 10, "EGLDUSDT": 10, "KAVAUSDT": 10, "JASMYUSDT": 10, "DODOBUSD": 10, "ZECUSDT": 10,
                 "VETUSDT": 10, "BATUSDT": 10, "ALICEUSDT": 10, "RAYUSDT": 10, "BANDUSDT": 10, "RENUSDT": 10, "XLMUSDT": 10,
                 "MTLUSDT": 10, "QTUMUSDT": 10, "ENJUSDT": 10, "YFIUSDT": 10, "NEOUSDT": 10, "GALUSDT": 10, "ARPAUSDT": 10,
                 "ENSUSDT": 10, "CELRUSDT": 10, "ATAUSDT": 10, "SKLUSDT": 10, "KNCUSDT": 10, "XRPBUSD": 10, "IOTXUSDT": 10,
                 "AVAXBUSD": 10, "ARUSDT": 10, "API3USDT": 10, "CHZUSDT": 10, "XEMUSDT": 10, "BLZUSDT": 10, "ROSEUSDT": 10,
                 "AUDIOUSDT": 10, "NEARBUSD": 10, "C98USDT": 10, "WOOUSDT": 10, "IMXUSDT": 10, "OCEANUSDT": 10,
                 "LRCUSDT": 10, "DOGEBUSD": 10, "HBARUSDT": 10, "DENTUSDT": 10, "CTKUSDT": 10, "MKRUSDT": 10, "DASHUSDT": 10, "IOSTUSDT": 10,
                 "CTSIUSDT": 10, "BNXUSDT": 10, "ZENUSDT": 10, "SXPUSDT": 10, "APEBUSD": 10, "CHRUSDT": 10, "HNTUSDT": 10,
                 "OMGUSDT": 10, "MASKUSDT": 10, "LINAUSDT": 10, "STMXUSDT": 10, "ANTUSDT": 10, "KSMUSDT": 10,
                 "CELOUSDT": 10, "ALPHAUSDT": 10, "FTTUSDT": 10, "FLOWUSDT": 10, "COTIUSDT": 10, "HOTUSDT": 10
}




# trading_ratio = {
#                  "BTCUSDT": 125, "ETHUSDT": 100, "BTCBUSD": 50, "UNFIUSDT": 25, "SOLUSDT": 50, "ETHBUSD": 50, "GMTUSDT": 50, "MATICUSDT": 50,
#                  "SRMUSDT": 50, "DYDXUSDT": 25, "1000SHIBUSDT": 50, "AVAXUSDT": 50, "ADAUSDT": 75, "BNBUSDT": 75, "NEARUSDT": 50,
#                  "SANDUSDT": 50, "XRPUSDT": 75, "DOTUSDT": 75, "APEUSDT": 50, "AAVEUSDT": 25, "OGNUSDT": 25, "TRBUSDT": 25, "SOLBUSD": 20,
#                  "DOGEUSDT": 50, "UNIUSDT": 25, "LINKUSDT": 75, "FTMUSDT": 25, "AXSUSDT": 50, "CRVUSDT": 50, "ONEUSDT": 25,
#                  "GALABUSD": 20, "WAVESUSDT": 50, "LTCUSDT": 75, "ATOMUSDT": 25, "RUNEUSDT": 50, "TRXUSDT": 25, "GALAUSDT": 25, "STORJUSDT": 50,
#                  "COMPUSDT": 50, "BCHUSDT": 75, "MANAUSDT": 50, "BAKEUSDT": 50, "RLCUSDT": 50, "LUNA2BUSD": 20, "1000LUNCBUSD": 20,
#                  "ICPBUSD": 20, "ETCUSDT": 75, "ONTUSDT": 50, "FILUSDT": 50, "XTZUSDT": 50, "FLMUSDT": 25, "GMTBUSD": 20, "1INCHUSDT": 50,
#                  "BNBBUSD": 20, "EOSUSDT": 75, "GRTUSDT": 50, "ZILUSDT": 25, "LITUSDT": 25, "PEOPLEUSDT": 25, "BELUSDT": 25, "RSRUSDT": 25,
#                  "SUSHIUSDT": 25, "OPUSDT": 25, "THETAUSDT": 50, "SNXUSDT": 25, "XMRUSDT": 50, "ALGOUSDT": 25,
#                  "GTCUSDT": 50, "ZRXUSDT": 50, "ANCBUSD": 20, "ADABUSD": 20, "EGLDUSDT": 50, "KAVAUSDT": 50, "JASMYUSDT": 25, "DODOBUSD": 20, "ZECUSDT": 50,
#                  "VETUSDT": 25, "BATUSDT": 50, "ALICEUSDT": 25, "RAYUSDT": 25, "BANDUSDT": 50, "RENUSDT": 50, "XLMUSDT": 50,
#                  "MTLUSDT": 50, "QTUMUSDT": 50, "ENJUSDT": 50, "YFIUSDT": 50, "NEOUSDT": 50, "GALUSDT": 25, "ARPAUSDT": 25,
#                  "ENSUSDT": 25, "CELRUSDT": 25, "ATAUSDT": 25, "SKLUSDT": 50, "KNCUSDT": 50, "XRPBUSD": 20, "IOTXUSDT": 25,
#                  "AVAXBUSD": 20, "ARUSDT": 25, "API3USDT": 25, "CHZUSDT": 50, "XEMUSDT": 50, "BLZUSDT": 25, "ROSEUSDT": 25,
#                  "AUDIOUSDT": 25, "NEARBUSD": 20, "C98USDT": 25, "WOOUSDT": 25, "IMXUSDT": 25, "OCEANUSDT": 50,
#                  "LRCUSDT": 25, "DOGEBUSD": 20, "HBARUSDT": 50, "DENTUSDT": 50, "CTKUSDT": 50, "MKRUSDT": 50, "DASHUSDT": 50, "IOSTUSDT": 50,
#                  "CTSIUSDT": 25, "BNXUSDT": 50, "ZENUSDT": 50, "SXPUSDT": 50, "APEBUSD": 20, "CHRUSDT": 50, "HNTUSDT": 50,
#                  "OMGUSDT": 25, "MASKUSDT": 25, "LINAUSDT": 50, "STMXUSDT": 50, "ANTUSDT": 25, "KSMUSDT": 50,
#                  "CELOUSDT": 25, "ALPHAUSDT": 50, "FTTUSDT": 25, "FLOWUSDT": 25, "COTIUSDT": 50, "HOTUSDT": 50
# }