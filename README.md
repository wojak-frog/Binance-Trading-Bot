# Binance_Trading_Bot
a Binance crypto trading bot which buys on news
<p><h1>Requirements:</h1><p>
  - requests <br>
  - BeautifulSoup <br>
  - Binance API  (pip install python-binance)  <br>
  
  
  
<p><h1>Imports and connecting:</h1><p>
  
`import requests
from bs4 import BeautifulSoup as BS
from binance.client import Client
client = Client(' ',' ') ` 
<br>

in the first and second line, we import `requests` and `bs4` from `BeautifulSoup` to be able to extract the HTML syntax of Binance news webpage. <br>
After that, you need to connect your Binance.com account to the bot (i suggest to use a demo account, not your main trading account): `client = Client(' ',' ')` . inside the single/double you input your keys. To generate the API keys and and assign relevant permissions, tap <a href='https://www.binance.com/en/support/articles/360002502072'> HERE</a><br>
