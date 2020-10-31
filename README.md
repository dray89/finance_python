My first Python coding project. Yes, I've recreated the wheel here as there are many programs to scrape Yahoo Finance. Nevertheless, recreating the wheel is a great way to learn how to code.

Yahoo Finance has changed its website since this was first created. Thus, it can no longer scrape the financials tab of the Yahoo Finance website. Nevertheless, it can still scrape price and dividend history, statistics, holders, options, and analysis tabs. 

I haven't had time to really maintain the code. However as of mid-October 2020, I'm doing some maintenance. 
 
Yahoo Finance: Just added multithreading to pull years of price and dividend history data (more than 100 rows is the standard for any given timeframe). Also scrapes sector, description, current price, analysis, and statistics tab. 

Nasdaq: Nasdaq earnings and dividend calendars

TMX: TMX used to provide a free API to pull data in json format --- but it has been shut down and now they are charging for access. Thus, this code no longer works, but it was a pretty easy project while it lasted. There are third party options to access this data like https://www.programmableweb.com/api/intrinio-real-time-canadian-stock-prices-tmx-tsx.

TDAmeritrade API: There's still some work I need to do with it like setting it up to renew auth codes upon expiration to avoid me having to do this manually. I'm putting these "to do's" on my calendar in the future.
