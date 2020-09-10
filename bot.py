import requests
from bs4 import BeautifulSoup as BS

from binance.client import Client
client = Client(' ',' ') #put your keys here

coins = ['LTC', 'BNB', 'NEO', 'BCC', 'GAS', 'HSR', 'MCO', 'WTC', 'LRC', 'QTUM', 'YOYO', 'OMG', 'ZRX', 'STRAT', 'SNGLS', 'BQX', 'KNC', 'FUN', 'SNM',
         'IOTA', 'LINK', 'XVG', 'SALT', 'MDA', 'MTL', 'SUB', 'EOS', 'SNT', 'ETC', 'MTH', 'ENG', 'DNT', 'ZEC', 'BNT', 'AST', 'DASH', 'OAX', 'ICN', 'BTG', 'EVX',
         'REQ', 'VIB', 'TRX', 'POWR', 'ARK', 'XRP', 'MOD', 'ENJ', 'STORJ', 'VEN', 'KMD', 'RCN', 'NULS', 'RDN', 'XMR', 'DLT', 'AMB', 'BAT', 'BCPT', 'ARN',
         'GVT', 'CDT', 'GXS', 'POE', 'QSP', 'BTS', 'XZC', 'LSK', 'TNT', 'FUEL', 'MANA', 'BCD', 'DGD', 'ADX', 'ADA', 'PPT', 'CMT', 'XLM', 'CND', 'LEND',
         'WABI', 'TNB', 'WAVES', 'GTO', 'ICX', 'OST', 'ELF', 'AION', 'NEBL', 'BRD', 'EDO', 'WINGS', 'NAV', 'LUN', 'TRIG', 'APPC', 'VIBE', 'RLC', 'INS',
         'PIVX', 'IOST', 'CHAT', 'STEEM', 'NANO', 'VIA', 'BLZ', 'AE', 'AEBNB', 'RPX', 'NCASH', 'POA', 'ZIL', 'ONT', 'STORM', 'XEM', 'WAN', 'WPR', 'QLC',
         'SYS', 'GRS', 'CLOAK', 'GNT', 'LOOM', 'BCN', 'REP', 'TUSD', 'TUSD', 'ZEN', 'SKY', 'CVC', 'THETA', 'IOTX', 'QKC', 'AGI', 'NXS', 'DATA', 'SC', 'SCBNB',
         'NPXS', 'KEY', 'NAS', 'MFT', 'DENT', 'ARDR', 'HOT', 'VET', 'DOCK', 'POLY', 'PHX', 'HC', 'GO', 'GOBNB', 'PAX', 'RVN', 'DCR', 'MITH', 'BCHSV', 'PAX',
         'REN', 'USDC', 'BTT', 'USDS', 'ONG', 'FET', 'CELR', 'MATIC', 'ATOM', 'PHB', 'TFUEL', 'ONE', 'FTM', 'B', 'ALGO', 'ERD', 'DOGE', 'DUSK', 'ANKR', 'WIN',
         'COS', 'COCOS', 'TOMO', 'PERL', 'CHZ', 'BAND', 'BUSD', 'BEAM', 'XTZ', 'HBAR', 'NKN', 'STX', 'KAVA', 'NGN', 'ARPA', 'CTXC', 'BCH', 'RUB', 'TROY', 'VITE',
         'FTT', 'TRY', 'EUR', 'OGN', 'DREP', 'TCT', 'WRX', 'LTO', 'MBL', 'COTI', 'STPT', 'ZAR', 'BKRW', 'SOL', 'IDRT', 'CTSI', 'HIVE', 'CHR', 'MDT', 'STMX', 'CRV']


trigger = ['Won', 'Win', 'Lucky'] # the positive words used in Binance announcements which trigger a buy order
saved_data = []

print("[*] connected to Binance...")
while True:
    r = requests.get(
        'https://www.binance.com/en/support/announcement/c-49?navId=49') #latest announcements section for binance.com
    html = BS(r.content, 'html.parser')
    to_fetch = []
    for link in html.find_all('a'):
                  
        link_text = link.get('href')
        if str(link_text).startswith('/en/support/articles/'):
            to_fetch.append(list(link_text.replace('/en/support/articles/', '').split('-')))


    for x in to_fetch:
        x.pop(0)
        x = to_fetch[0]

        for i in x:
            if i in trigger:
                for coin in coins:
                    if coin in x:
                        coin_ticker = coin
                  
                if x in saved_data:
                    pass
                else:
                    saved_data.append(x)
                    print('[*] Possible Trade: ', ' '.join(x), f'Trade {coin_ticker}')
                    print(client.get_ticker(symbol=(f'{coin_ticker}BTC'))['askPrice'])

            elif i == 'Mainnet':
                if 'Upcoming' in x:
                    for coin in coins:
                        if coin in x:
                            coin_ticker = coin
                    if x in saved_data:
                        pass
                    else:
                        saved_data.append(x)
                        print('[*] Possible Trade: ', ' '.join(x), f'Trade {coin_ticker}')
                        print(client.get_ticker(symbol=(f'{coin_ticker}BTC'))['askPrice'])

            elif i == 'Perpetual':

                if 'Launch' in x:
                    for coin in coins:
                        if coin in x:
                            coin_ticker = coin
                        else:
                            coin_ticker = 'unknown'
                    if x in saved_data:
                        pass
                    else:
                        saved_data.append(x)
                        print('[*] Possible Trade: ', ' '.join(x), f'Trade {coin_ticker}')
                        print(client.get_ticker(symbol=(f'{coin_ticker}BTC'))['askPrice'])


                  #get pair's latest infos and convert the price
                    info = client.get_symbol_info(f'{coin_ticker}BTC')
                    #print(info)
                    btc = client.get_ticker(symbol=('BTCUSDT'))['lastPrice']
                    token = client.get_ticker(symbol=(f'{coin_ticker}BTC'))
                    
                    token_price = token['lastPrice']
                    trade_amount = 0.5 / float(btc) / float(token_price)
                    
                    token_askPrice = token['askPrice']





                    #order = client.order_limit_buy(      ######  input the buy function when you are ready to run the bot ######
                        #symbol= 'TRXBNB',
                        #quantity= 50,
                        #price=0.000981)



                    #print(order)







