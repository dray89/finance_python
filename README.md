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

        Example:
---------------------------------------------------------------------------------------------
        from datetime import date
        symbol = "aapl"
        start = date(2018, 8, 14)
        end = date(2019, 8, 14)
        apple = stock(symbol, start, end)

        apple.attributes #lists attributes and additional methods.

        apple.statistics

--------------------------------------------------------------------------------------------
In progress:
---------------------------------------------------------------------------
cashflow.py: scrapes cashflow information from yahoo.
analysis.py: scrapes analysis information from yahoo.
financials.py: scrapes financial information from yahoo.
balance_sheet.py: scrapes balance_sheet information.

scraper.py: Scrapers used throughout each of these files live in scraper.py
    This file contains scrapers for every tab at the url finance.yahoo.com/quotes/symbol


calendar.py: This is a minor accompanying file which will scrape the earnings calendar.
    I have spent less time testing and optimzing this for use, but if anyone is interested in
    expanding upon it, please feel free to reach out to me with questions, concerns, and comments.


I’ve tried to keep it simple and easy to learn how to use.
Remember: It is still in testing stages. So, feel free to use and contribute to the project.
If you have any questions, feel free to reach out.

-----------------------------------------------------------------------------------------------

Planned Upgrades:
I want to set it up to SQLlite or Postgres to store the stock information.

-----------------------------------------------------------------------------------------------

------------------------------------------------------------------------------------------
Full Disclosure:
------------------------------------------------------------------------------------------
    This program is still in the process of being developed which means the version posted
    may go down from time to time. This will happen if I mistakenly merge edits to GitHub
    too quickly before the files have been (more or less) fully debugged.

    I promise to try not to do that often. To be safe, please keep a download of the files on your computer
    and do not overwrite unless you are certain that the scraper is up-to-date and debugged (more or less).

    I am using the scraper daily during the course of my work with The Motley Fool as a Toronto Stock Exchange
    reporter. Thus, everyday I test the program on different stocks. When I run into a new error, or think of
    a way to make the tool more efficient, I will begin to make serious updates.

    During this time of debugging and code optimization, please feel free to send pull requests with
    suggestions on how to improve the code for speed, ease-of-use, or minimize errors.