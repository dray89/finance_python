# finance_python

Hi There!

Welcome to the best open-source software to scrape finance data from Yahoo.

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

-------------------------------------------------------------------------------------------
Instructions
---------------------------------------------------------------------------------------------
stock_scraper_v3.py: Contains the primary command in the program, get_data()
    running the class, get_data(), will set attributes for price history, dividends history, industry description,
                           company description, and a balance sheet object.
                           
financials.py: All Self-Contained Private Functions. This file feeds into balance_sheet.py
    This file scrapes the data from yahoo and cleans it into dataframes.


balance_sheet.py: As of 8/14/2019, this file is temporarily out of service.
    Critical updates are being made to avoid setting too many attributes outside of dataframes.
    Thus, it may be buggy from time to time as it is optimized and cleaned.


industry.py: As of 8/14/2019, this file is temporarily out of service
    Critical updates are being made to streamline concatination and prepare the
    resulting data frames for calculations.


scrape.py: Scrapers used throughout each of these files live in scrape.py
    This file contains scrapers for every tab at the url finance.yahoo.com/quotes/symbol


calendar.py: This is a minor accompanying file which will scrape the earnings calendar.
    I have spent less time testing and optimzing this for use, but if anyone is interested in
    expanding upon it, please feel free to reach out to me with questions, concerns, and comments.


clean_dfs.py: This is a new capability. Before, it lived in the industry file happily.
              However, I think it may be better if we dropna'd/reformatted numstrings
              in the dataframe after the industry merge to prevent later errors.


I’ve tried to keep it simple and easy to learn how to use. 
Remember: It is still in testing stages. So, feel free to use and contribute to the project.
If you have any questions, feel free to reach out.

-----------------------------------------------------------------------------------------------

Planned Upgrades:
I want to set it up to SQLlite or Postgres to store the stock information.

-----------------------------------------------------------------------------------------------

