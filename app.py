from flask import Flask

from api.ScrapeApi import ScrapePPApi_Router
from api.UserApi import UserRegisterApi_Router, UserLoginApi_Router

app = Flask(__name__)

# Scraping Routes
app.register_blueprint(ScrapePPApi_Router, url_prefix="/spp_api")

# Account Routes
app.register_blueprint(UserRegisterApi_Router, url_prefix="/ar_api")
app.register_blueprint(UserLoginApi_Router, url_prefix="/al_api")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
