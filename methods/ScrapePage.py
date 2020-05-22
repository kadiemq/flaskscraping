from bs4 import BeautifulSoup

from Constants import DIV, ID, DATA_METRICS, ASIN_PRICE, ASIN_ASIN, CONTENT, TITLE, NAME, META, SPAN, PRICE_BLOCK, \
    LANDING_IMAGE, IMAGE_DATA, ASIN_COUNTRY

from classes.Product import Product


def method_ScrapeProductPage(data, url):
    soup = BeautifulSoup(data, features="html.parser")
    product = Product()

    product.url = url

    # # Price
    # price = soup.find(DIV, {ID: DATA_METRICS})[ASIN_PRICE]
    # product.price = float(price)
    #
    # # ASIN
    # ASIN = soup.find(DIV, {ID: DATA_METRICS})[ASIN_ASIN]
    # product.asin = ASIN
    #
    # # Title
    # title = soup.find(META, {NAME: TITLE})[CONTENT]
    # product.title = title
    #
    # # Price String
    # price_string = soup.find(SPAN, {ID: PRICE_BLOCK}).text
    # product.price_string = price_string
    #
    # # Img Url
    # img_url = soup.find('', {ID: LANDING_IMAGE})[IMAGE_DATA]
    # product.image_url = img_url
    #
    # # Country
    # country = soup.find('', {ID: DATA_METRICS})[ASIN_COUNTRY]
    # product.country = country
    #
    # return product

    try:

        # Price
        price = soup.find(DIV, {ID: DATA_METRICS})[ASIN_PRICE]
        product.price = float(price)

        # ASIN
        ASIN = soup.find(DIV, {ID: DATA_METRICS})[ASIN_ASIN]
        product.asin = ASIN

        # Title
        title = soup.find(META, {NAME: TITLE})[CONTENT]
        product.title = title

        # Price String
        price_string = soup.find(SPAN, {ID: PRICE_BLOCK}).text
        product.price_string = price_string

        # Img Url
        img_url = soup.find('', {ID: LANDING_IMAGE})[IMAGE_DATA]
        product.image_url = img_url

        # Country
        country = soup.find('', {ID: DATA_METRICS})[ASIN_COUNTRY]
        product.country = country

    except TypeError:

        return False

    else:
        return product
