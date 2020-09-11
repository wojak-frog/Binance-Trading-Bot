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
After that, you need to connect your Binance.com account to the bot (i suggest to use a demo account, not your main trading account): `client = Client(' ',' ')` . inside the single/double quote you input your keys. To generate the API keys and assign relevant permissions, tap <a href='https://www.binance.com/en/support/articles/360002502072'> HERE</a><br>

<p><h1>Coins list and trigger keywords:</h1></p> <br>
I have avoided the integration of any NLP or ML related keywords analysis methods to make the code's execution faster. Yes it may have weak points specially if Binanace changes its most used words in positive news, so if you used NLP, the analysis of news might be more precise, but it's up to you. You can kepp following Binance announcements and upgrade the  `trigger` list's keywords as you wish. <br>

Regarding the `coins` list, i have added the most recent added tokens and coins (before the DeFi hype). Again, it's up to you to keep this list, or reduce it to watch less pairs (like your favorite pairs where you may automate trades basing on its news) <br>

<p><h1>Extracting announcements:</h1></p><br>
the code below loops over all `<a> </a>`  HTML elements in Binance announcement page: <br>
for link in html.find_all('a'):<br>

        for link in html.find_all('a'):

<br>After that, using BeautifulSoop again, we get the `href` or links inserted in the `<a> </a>` element which result in extracting the announcement title: <br>
      `link_text = link.get('href')`
      
<br>The next step is to use a condition statement `if` to check if the announcement's link start with `/en/support/articles/`: <br>
      `if str(link_text).startswith('/en/support/articles/'):`
      
   if `True` , we append to `to_fetch` list the 'clean' announcement title as follow: <br> <br>
              - `/en/support/articles/` is removed from the title by replacing it with an empty string: `link_text.replace('/en/support/articles/', '')` <br><br>
              - all title's words are added to a list then splitted on `-` : `list(link_text.replace('/en/support/articles/', '').split('-'))` <br><br>
              - finally the result (a list) is added to `to_fetch` list: `to_fetch.append(list(link_text.replace('/en/support/articles/', '').split('-')))` <br><br>
