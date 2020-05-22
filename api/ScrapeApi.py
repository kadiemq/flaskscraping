from concurrent.futures.thread import ThreadPoolExecutor

from flask import Blueprint, request, jsonify, g

from functions.Middleware import middleware_CheckUser
from functions.fn_ScrapeProductPage import function_ScrapeProductPage

ScrapePPApi_Router = Blueprint('router', __name__)


# Base Route /spp_api
@ScrapePPApi_Router.route('/', methods=['GET'])
@middleware_CheckUser(request)
def index():
    url = request.args.get('url')
    if not g.logged_in:
        return g.message
    if not g.is_admin:
        return g.message
    executor = ThreadPoolExecutor()
    t = executor.submit(function_ScrapeProductPage, url)
    response = t.result()

    # print(f'Number of active before threads: {threading.active_count()}')
    #
    # t = threading.Thread(target=ScrapeProductPage, args=[url])
    # t.start()
    # t.join()
    # response = que.get()

    # return jsonify(request.environ['REMOTE_ADDR'], request.remote_addr, response)
    return jsonify(response)
