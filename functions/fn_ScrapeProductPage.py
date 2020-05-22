import queue
import time

from methods.DatabaseMethods.DoExist import DoExist
from methods.DatabaseMethods.InsertDB import InsertDB
from methods.DatabaseMethods.UpdateProduct import UpdateProduct
from methods.ScrapePage import method_ScrapeProductPage
from methods.loadPage import LoadPage

que = queue.Queue()


def function_ScrapeProductPage(url):
    loadPageStart = time.perf_counter()
    PageHtml = LoadPage(url)
    loadPageFinish = time.perf_counter()
    print(f'time needed to load page: {round(loadPageFinish - loadPageStart, 2)}')

    #############################################################
    ScrapePageFullStart = time.perf_counter()
    product = method_ScrapeProductPage(PageHtml, url)
    ScrapePageFullFinish = time.perf_counter()
    print(f'time needed to scrape page: {round(ScrapePageFullFinish - ScrapePageFullStart, 2)}')

    #############################################################
    if product:

        DatabaseWorkStart = time.perf_counter()
        DoExistsTest = DoExist('product', product)

        if DoExistsTest:
            # Update Price
            priceChanged, productId = UpdateProduct(product)
        else:
            # Add Products
            productId = InsertDB('product', product)
            priceChanged = False

        DatabaseWorkFinish = time.perf_counter()
        print(f'time needed for database work: {round(DatabaseWorkFinish - DatabaseWorkStart, 2)}')

        response = {'Product Info': product.__dict__,
                    'Database Info': {'Did_Exist': DoExistsTest, 'productId': productId,
                                      'Price_Changed': priceChanged}}
        return response

    else:
        return 'An error happened during scraping.'
