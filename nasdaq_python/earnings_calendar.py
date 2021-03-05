from datetime import datetime, date


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
        df = self.dict_to_df(dicti)
        df['Date'] = date(self.year, self.month, int(day))
        self.calendars.append(df)
        return df
    
'''    
if __name__ == '__main__':
    import pandas
    import concurrent.futures
    import calendar
    
    year = 2020
    month = 10

    # get number of days in month
    days_in_month = calendar.monthrange(year, month)[1]

    # create calendar object
    march = Earnings_Calendar(year, month)

    # define lambda function to iterate over list of days
    function = lambda days: march.earnings_calendar(days)

    # define iterator as a list of integers between 1 and the number of days in the month
    #iterator = list(range(21, days_in_month + 1))
    iterator = list(range(22, 23))

    # Scrape calendar for each day of the month
    objects = list(map(function, iterator))

    # concatenate all the calendars in the class attribute
    df = pandas.concat(march.calendars)

    # set the dataframe's row index to the company name
    df = df.set_index('Date')
'''