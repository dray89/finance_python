# -*- coding: utf-8 -*-
"""
Created on Wed Oct 30 16:49:25 2019

@author: rayde
"""


from __future__ import division
from __future__ import print_function
from __future__ import absolute_import
from basic import basic

from .progressbar import ProgressBar, Percentage, Bar, RotatingMarker, ETA, FileTransferSpeed
from .utils import download_worker_fn
from .exceptions import DirectoryAccessError, DirectoryCreateError, PageLoadError
from setproctitle import setproctitle
from concurrent.futures import ThreadPoolExecutor
import threading
import sys

def main():
    """ Called when the command is executed
        Calls the function that starts the script
        handles KeyboardInterrupt
    """
    try:
        console_main()
    except KeyboardInterrupt:
        print ("Scraping stopped by user.")

def console_main():
    """ This function handles all the console action. """
    setproctitle('image-scraper')
    '''
    The setproctitle module allows a process to change its title (as displayed by system tools such as ps and top).
    Changing the title is mostly useful in multi-process systems, for example when a master process is forked: changing the children’s title allows to identify the task each process is busy with. The technique is used by PostgreSQL and the OpenSSH Server for example.
    The procedure is hardly portable across different systems. 
    PostgreSQL provides a good multi-platform implementation: this module is a Python wrapper around PostgreSQL code.
    '''
    scraper = basic()
    scraper.get_arguments()
    print("\nImageScraper\n============\nRequesting page....\n")
    try:
        scraper.get_html()
    except PageLoadError as err:
        if err.status_code is None:
            print("ImageScraper is unable to acces the internet.")
        else:
            print("Page failed to load. Status code: {0}".format(err.status_code))
        sys.exit()

    scraper.get_img_list()

    if len(scraper.images) == 0:
        sys.exit("Sorry, no images found.")
    if scraper.no_to_download is None:
        scraper.no_to_download = len(scraper.images)

    print("Found {0} images: ".format(len(scraper.images)))

    try:
        scraper.process_download_path()
    except DirectoryAccessError:
        print("Sorry, the directory can't be accessed.")
        sys.exit()
    except DirectoryCreateError:
        print("Sorry, the directory can't be created.")
        sys.exit()

    if scraper.dump_urls:
        for img_url in scraper.images:
            print(img_url)

    status_flags = {'count': 0, 'percent': 0.0, 'failed': 0, 'under_min_or_over_max_filesize': 0}
    widgets = ['Progress: ', Percentage(), ' ', Bar(marker=RotatingMarker()),
               ' ', ETA(), ' ', FileTransferSpeed()]
    pbar = ProgressBar(widgets=widgets, maxval=100).start()
    pool = ThreadPoolExecutor(max_workers=scraper.nthreads)
    status_lock = threading.Lock()
    for img_url in scraper.images:
        if status_flags['count'] == scraper.no_to_download:
            break
        pool.submit(download_worker_fn, scraper, img_url, pbar, status_flags, status_lock)
        status_flags['count'] += 1
    pool.shutdown(wait=True)
    pbar.finish()
    print("\nDone!\nDownloaded {0} images\nFailed: {1}\n".format(
        status_flags['count']-status_flags['failed']-status_flags['under_min_or_over_max_filesize'],
        status_flags['failed']))
    return