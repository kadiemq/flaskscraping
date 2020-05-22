class Product:
    def __init__(self):
        self._title = None
        self._price = None
        self._price_string = None
        self._asin = None
        self._url = None
        self._image_url = None
        self._country = None
        pass

    def __repr__(self):
        return repr(self.__dict__)
        # return repr({'title': {self._title}, 'price': {self._price}, 'price_string': {self._price_string}})
        # return self.title

    # Getter
    @property
    def title(self):
        return self._title

    @property
    def price(self):
        return self._price

    @property
    def asin(self):
        return self._asin

    @property
    def price_string(self):
        return self._price_string

    @property
    def url(self):
        return self._url

    @property
    def image_url(self):
        return self._image_url

    @property
    def country(self):
        return self._country

    # Setters
    @title.setter
    def title(self, title):
        self._title = title

    @price.setter
    def price(self, price):
        self._price = price

    @asin.setter
    def asin(self, asin):
        self._asin = asin

    @price_string.setter
    def price_string(self, price_string):
        self._price_string = price_string

    @url.setter
    def url(self, url):
        self._url = url

    @image_url.setter
    def image_url(self, url):
        self._image_url = url

    @country.setter
    def country(self, country):
        self._country = country
