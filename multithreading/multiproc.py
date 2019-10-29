# -*- coding: utf-8 -*-
"""
Created on Tue Oct 29 06:59:19 2019

@author: rayde
"""


import logging
import os
from functools import partial
from multiprocessing.pool import Pool
from time import time

from download import setup_download_dir, get_links, download_link


logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
logging.getLogger('requests').setLevel(logging.CRITICAL)
logger = logging.getLogger(__name__)


def main():
    ts = time()
    client_id = os.getenv('IMGUR_CLIENT_ID')
    if not client_id:
        raise Exception("Couldn't find IMGUR_CLIENT_ID environment variable!")
    download_dir = setup_download_dir()
    links = get_links(client_id)
    download = partial(download_link, download_dir)
    with Pool(4) as p:
        p.map(download, links)
    logging.info('Took %s seconds', time() - ts)


if __name__ == '__main__':
    main()