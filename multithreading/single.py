# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 06:45:28 2019

@author: rayde
"""


import logging
import os
from time import time

from download import setup_download_dir, get_links, download_link

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

def main():
    ts = time()
    client_id = os.getenv('IMGUR_CLIENT_ID')
    if not client_id:
        raise Exception("Couldn't find IMGUR_CLIENT_ID environment variable!")
    download_dir = setup_download_dir()
    links = get_links(client_id)
    for link in links:
        download_link(download_dir, link)
    logging.info('Took %s seconds', time() - ts)

if __name__ == '__main__':
    main()