from datetime import datetime
import pandas 
from nasdaq_python.nasdaq_main import NasdaqData

class Earnings_Calendar(NasdaqData):
    # class attributes
    calendars = []
    url = 'https://api.nasdaq.com/api/calendar/earnings'

    def __init__(self, year, month):
        '''
      Parameters
      ----------
      year : year int
      month : month int

      Returns
      -------
      Sets instance attributes for year and month of object.
      Empty calendars list is a class attribute.

        '''
        # instance attributes
        self.year = int(year)
        self.month = int(month)

    def date_str(self, day):
        date_obj = datetime(self.year, self.month, day)
        date_str = date_obj.strftime(format='%Y-%m-%d')
        return date_str

    def earnings_calendar(self, day):
        '''
        Combines the above methods into one method.

        Parameters
        ----------
        day : day of the month as string or number.

        Returns
        -------
        dictionary : Returns a JSON dictionary with keys
        dictionary.keys() => data, message, status

        Next Levels:
        dictionary['data'].keys() => calendar, timeframe
        dictionary['data']['calendar'].keys() => headers, rows
        dictionary['data']['calendar']['headers'] => column names
        dictionary['data']['calendar']['rows'] => dictionary list

        '''
        self.day = day
        date_str = self.date_str(day)
        dicti = self.scraper(self.url, kwargs={'date':date_str})
        self.dict_to_df(dicti)
        return dicti
    
    
if __name__ == '__main__':
    import calendar
    year = 2020
    month = 3

    # get number of days in month
    days_in_month = calendar.monthrange(year, month)[1]

    # create calendar object
    march = Earnings_Calendar(year, month)

    # define lambda function to iterate over list of days
    function = lambda days: march.earnings_calendar(days)

    # define iterator as a list of integers between 1 and the number of days in the month
    iterator = list(range(1, days_in_month + 1))

    # Scrape calendar for each day of the month
    objects = list(map(function, iterator))

    # concatenate all the calendars in the class attribute
    df = pandas.concat(march.calendars)

    # Drop any rows with missing data
    df = df.dropna(how='any')

    # set the dataframe's row index to the company name
    df = df.set_index('name')

    '''    
    year = 2020 
    month = 3
    day = 2
    date = datetime(year, month, day)
    date = date.strftime(format='%Y-%m-%d')    

    hdrs =  {'Accept': 'application/json, text/plain, */*',
                 'DNT': "1",
                 'Origin': 'https://www.nasdaq.com/',
                 'Sec-Fetch-Mode': 'cors',
                 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0)'}

    urls = 'https://api.nasdaq.com/api/calendar/earnings'
    page = requests.get(urls, headers=hdrs, params=date)
    dictionary = page.json()

    rows = dictionary.get('data').get('rows')
    rows 

    cal = pandas.DataFrame(rows)
    cal

    df = cal.dropna(how='any')    
    df = df.set_index('name')
    '''