import bcrypt


class User:
    def __init__(self, email=None, first_name=None, last_name=None, password=None):
        self._email = email
        self._first_name = first_name
        self._last_name = last_name
        self._password = password
        # self._url = None
        # self._image_url = None
        # self._country = None
        pass

    def __repr__(self):
        return repr(self.__dict__)

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        return

    def check_password(self, password):
        match = bcrypt.checkpw(password.encode('utf8'), self._password.encode('utf8'))

        if match:
            return True
        else:
            return False

    # Getter
    @property
    def email(self):
        return self._email

    @property
    def first_name(self):
        return self._first_name

    @property
    def last_name(self):
        return self._last_name

    @property
    def password(self):
        return self._password

    # @property
    # def url(self):
    #     return self._url
    #
    # @property
    # def image_url(self):
    #     return self._image_url
    #
    # @property
    # def country(self):
    #     return self._country

    # Setters
    @email.setter
    def email(self, email):
        self._email = email

    @first_name.setter
    def first_name(self, first_name):
        self._first_name = first_name

    @last_name.setter
    def last_name(self, last_name):
        self._last_name = last_name

    @password.setter
    def password(self, password):
        unhashed_password = password.encode('utf8')

        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(unhashed_password, salt)
        self._password = hashed_password.decode("utf-8")

        # @url.setter
    # def url(self, url):
    #     self._url = url
    #
    # @image_url.setter
    # def image_url(self, url):
    #     self._image_url = url
    #
    # @country.setter
    # def country(self, country):
    #     self._country = country
