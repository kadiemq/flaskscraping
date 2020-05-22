import time

import requests
from fake_useragent import UserAgent

import queue


# q = queue.Queue()


def LoadPage(url):
    # url = 'https://www.amazon.ae/Apple-iPhone-Pro-FaceTime-International/dp/B07Y3L591B/ref=sr_1_1?keywords=iphone&qid=1589845523&sr=8-1'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) '
                      'Chrome/39.0.2171.95 Safari/537.36'}
    ua = UserAgent()
    hdr = {'User-Agent': ua.random,
           'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
           'Accept-Charset': 'ISO-8859-1,utf-8;q=0.7,*;q=0.3',
           'Accept-Encoding': 'none',
           'Accept-Language': 'en-US,en;q=0.8',
           'Connection': 'keep-alive'}

    response = requests.get(url, headers=hdr)

    data = response.text
    return data
    # q.put(data)
    # print('Finished Scrapping')
    # print(data)

    # print('Started Sleeping')
    # time.sleep(10)
    # print("Finished Sleeping.")
