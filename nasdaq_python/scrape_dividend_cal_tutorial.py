# -*- coding: utf-8 -*-
"""
Created on Fri Jan 17 16:53:24 2020

@author: rayde
"""

import pandas, requests, datetime, calendar

class dividend_calendar:
    #class attributes 
    calendars = [] 
    url = 'https://api.nasdaq.com/api/calendar/dividends'
    hdrs =  {'Accept': 'application/json, text/plain, */*',
                 'DNT': "1",
                 'Origin': 'https://www.nasdaq.com/',
                 'Sec-Fetch-Mode': 'cors',
                 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0)'}

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
          #instance attributes
          self.year = int(year)
          self.month = int(month)
      
    def scraper(self, date):
         '''
           Parameters
           - - - - - 
           url : URL string
           hdrs : Header information
           date: 
               
           Returns
           - - - -
           dictionary : Returns a JSON dictionary at a given URL.
         '''
         page = requests.get(self.url, headers=self.hdrs, params= {'date':date})
         dictionary = page.json()
         return dictionary
     
    
    def dict_to_df(self, dicti):
         '''
         Parameters
         ----------
         dicti : Output from the scraper method as input.
         
         Returns
         -------
         calendar : Dataframe of stocks with that exdividend date
         Appends the dataframe to one of the class attributes
         
         If the date is formatted, it will append a dataframe 
         to the calendars list (class attribute). Otherwise, it will 
         return an empty dataframe.         
         '''
         rows = dicti.get('data', dict({'calendar':{'rows':1}}))
         rows = rows.get('calendar',dict({'rows':1}))
         rows = rows.get('rows','')         
         calendar = pandas.DataFrame(rows)
         self.calendars.append(calendar)
         return calendar
     
    def date_str(self, day):
        date_obj = datetime.date(self.year, self.month, day)
        date_str = date_obj.strftime(format='%Y-%m-%d')     
        return date_str
            
    def calendar(self, day):
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
          dictionary = self.scraper(date_str)
          calendar = self.dict_to_df(dictionary)          
          return calendar 
           
if __name__ == '__main__':
    year = 2020
    month = 2
    
    #get number of days in month
    days_in_month = calendar.monthrange(year, month)[1]

    #create calendar object    
    february = dividend_calendar(year, month)

    #define lambda function to iterate over list of days     
    function = lambda days: february.calendar(days)
    
    #define iterator as a list of integers between 1 and the number of days in the month
    iterator = list(range(1,days_in_month+1))

    #Scrape calendar for each day of the month                    
    objects = list(map(function, iterator))

    #concatenate all the calendars in the class attribute
    df = pandas.concat(february.calendars)
    
    #Drop any rows with missing data
    df = df.dropna(how='any')
    
    #set the dataframe's row index to the company name
    df = df.set_index('companyName')
    
    '''    
    date = datetime.date(year, month, day=28)
    date = date.strftime(format='%Y-%m-%d')    
    
    api_params = {'date': '2020-02-3'}
    hdrs =  {'Accept': 'application/json, text/plain, */*',
                 'DNT': "1",
                 'Origin': 'https://www.nasdaq.com/',
                 'Sec-Fetch-Mode': 'cors',
                 'User-Agent': 'Mozilla/5.0 (Windows NT 10.0)'}
    
    urls = 'https://api.nasdaq.com/api/calendar/dividends'
    page = requests.get(urls, headers=hdrs, params=api_params)
    dictionary = page.json()
    
    rows = dictionary.get('data').get('calendar').get('rows')
    rows 
    
    cal = pandas.DataFrame(rows)
    cal

    df = cal.dropna(how='any')    
    df = df.set_index('companyName')
    '''