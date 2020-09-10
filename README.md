# Binance_Trading_Bot
a Binance crypto trading bot which buys on news
<p><h1>Requirements:</h1><p>
  - requests <br>
  - BeautifulSoup <br>
  - Binance API  (pip install python-binance)  <br>
  
  
  
<p><h1>Imports and connecting:</h1><p>
  
`import requests` <br>
`from bs4 import BeautifulSoup as BS` <br>
`from binance.client import Client` <br>
`client = Client(' ',' ') ` <br>
<br>

in the first and second line, we import `requests` and `bs4` from `BeautifulSoup` to be able to extract the HTML syntax of Binance news webpage. <br>
After that, you need to connect your Binance.com account to the bot (i suggest to use a demo account, not your main trading account): `client = Client(' ',' ')` . inside the single/double you input your keys. To generate the API keys and and assign relevant permissions, tap <a href='https://www.binance.com/en/support/articles/360002502072'> HERE</a><br>

<p><h1>Coins list and trigger keywords:</h1></p> <br>
I have avoided integrating and NLP or ML related keywords analysis methods to make the code's execution faster. Yes it may have weak points specially if Binanace changes its most used words in positive news, and if you use NLP the analysis of news might be more precise, but it's up to you. You can stay following Binance announcements and upgrade the `trigger` list as you wish.

Regarding the `coins` list, i have added the most recent added tokens and coins (before the DeFi hype). Again, it's up to you to keep this list, or reduce it to watch less pairs (like your favorite pairs where you may automate trades basing on its news)
