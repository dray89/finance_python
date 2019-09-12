# finance_python: NEW VERSION, Reorganized Classes

Hi There!

Welcome to the best open-source software to scrape finance data from Yahoo.

-------------------------------------------------------------------------------------------
Instructions
---------------------------------------------------------------------------------------------
stock.py: Contains the primary command in the program, stock()
    running the class, stock(), will set attributes for price history, dividends history, industry description,
                           and company description.

statistics.py: scrapes statistics information from yahoo. Feeds into method in stock.py.

cashflow.py: scrapes cashflow information from yahoo.

analysis.py: scrapes analysis information from yahoo.

financials.py: scrapes financial information from yahoo.

balance_sheet.py: scrapes balance_sheet information.

        Example:

        from datetime import date
        from stock import stock
        from industry import industry

        symbol = "aapl"
        start = date(2018, 8, 14)
        end = date(2019, 8, 14)
        apple = stock(symbol, start, end)

        apple.attributes #lists attributes and additional methods.

        apple.stats()
        apple.balance()
        apple.financial()
        apple.cash()
        apple.analyze()

        apple.attributes

        apple.statistics

        portfolio = portfolio()
        portfolio.financials(apple.fin_list)
        portfolio.cashflow(apple.cash_list)
        portfolio.statistics(apple.stats_list)
        portfolio.balance_sheet(apple.stats_list)

--------------------------------------------------------------------------------------------

scraper.py: Scrapers used throughout each of these files live in scraper.py
    This file contains scrapers for every tab at the url finance.yahoo.com/quotes/symbol


calendar.py: This is a minor accompanying file which will scrape the earnings calendar.
    I have spent less time testing and optimzing this for use, but if anyone is interested in
    expanding upon it, please feel free to reach out to me with questions, concerns, and comments.


I’ve tried to keep it simple and easy to learn how to use.
Remember: It is still in testing stages. So, feel free to use and contribute to the project.
If you have any questions, feel free to reach out.

-----------------------------------------------------------------------------------------------
