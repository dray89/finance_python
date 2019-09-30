# -*- coding: utf-8 -*-
"""
Created on Thu Jul 25 18:06:26 2019

@author: rayde
"""
import requests, pandas, lxml
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen
from lxml import html

class scraper:
    def __init__(self, symbol):
        self.symbol = symbol
        self.headers = {':authority': 'finance.yahoo.com' ,
                   ':method': 'GET',
                   ':path':' /_finance_doubledown/api/resource/finance.market-time?bkt=%5B%22d-qsp-fin-new%22%2C%22fd-mkt-ctrl%22%2C%22fin-mkt-ctrl%22%2C%22fdw-sr%22%5D&device=desktop&feature=adsMigration%2CcanvassOffnet%2CccOnMute%2CclientDelayNone%2Cdebouncesearch100%2CecmaModern%2CemptyServiceWorker%2CenableCMP%2CenableConsentData%2CenableTheming%2CenableNavFeatureCue%2CenableFeatureTours%2CenableFreeFinRichSearch%2CenableGuceJs%2CenableGuceJsOverlay%2CenablePortfolioPremium%2CenablePremiumSingleCTA%2CenablePremiumKeyStats%2CenablePremiumFinancials%2CenableFinancialsFeatureCue%2CenablePrivacyUpdate%2CenableVideoURL%2CnewContentAttribution%2CoathPlayer%2Cpremium35%2CrelatedVideoFeature%2CwebSocketStreamer%2CvideoNativePlaylist%2CnewLogo%2Clivecoverage%2CdarlaFirstRenderingVisible%2CenableTradeit%2CenableFeatureBar%2CenableSearchEnhancement%2CenableSingleRail%2CenableUserSentiment%2CenableBankrateWidget%2CenhanceAddToWL%2CsponsoredAds%2CenableTradeItLinkBrokerSecondaryPromo%2CpremiumPromoHeader%2CenableQspPremiumPromoSmall&intl=us&lang=en-US&partner=none&prid=cfv0qqheoukb7&region=US&site=finance&tz=America%2FNew_York&ver=0.102.2872&returnMeta=true',
                   ':scheme': 'https',
                   'accept': '*/*',
                   'accept-encoding': 'gzip, deflate, br',
                   'accept-language': 'en-US,en;q=0.9',
                   'cookie': 'APID=UP16ca3b02-e1d0-11e9-bc5a-0a100fd205b2; PRF=t%3DEMH.V%252BBCE.TO%252BMRC.TO%26qsp-fnncls-cue%3D1; APIDTS=1569673855; B=bkhlofheou8t7&b=3&s=85',
                   'dnt': 1,
                   'if-none-match': 'W/"161-E4ddOn0vlRx2CqtyPh0ecAoVLdo"',
                   'referer': 'https://finance.yahoo.com/quote/EMH.V/financials?p=EMH.V',
                   'sec-fetch-mode': 'cors',
                   'sec-fetch-site': 'same-origin',
                   'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/77.0.3865.90 Safari/537.36 x-requested-with: XMLHttpRequest'}

    def __general__(self, url):
        Client=urlopen(url)
        xml_page=Client.read()
        Client.close()
        soup_page=soup(xml_page,"xml")
        return soup_page

    def __table__(self, url):
        headers = self.headers
        page = requests.get(url, params = headers)
        tree = html.fromstring(page.content)
        table = tree.xpath('//table')
        table = list(map(lambda x: pandas.read_html(lxml.etree.tostring(table[x], method='xml'))[0], range(0,len(table))))
        return table
