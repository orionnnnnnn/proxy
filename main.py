import requests
from flask import Flask
from gevent import pywsgi
from flask_cors import CORS

api = ''
app = Flask(__name__)
CORS(app)


def get_ip(api):
    res = requests.get(api).json()
    if res['code'] == 0:
        ips = res['data']
        return ips
    else:
        return get_ip()


def test_proxy(url):
    proxies = {
        'http': url,
        'https': url
    }
    try:
        res = requests.get('http://httpbin.org/ip', proxies=proxies, timeout=5)
        if res.status_code == 200:
            print(res.text)
            return True
        else:
            return False
    except Exception as e:
        return False


def find_valid_proxy(api):
    ips = get_ip(api)
    for ip in ips:
        if test_proxy(ip['ip']):
            return ip['ip']
    return find_valid_proxy()


def main():
    app.logger.disabled = True
    server = pywsgi.WSGIServer(('0.0.0.0', 5555), app)
    server.serve_forever()


@app.route('/getProxy', methods=['GET'])
def api1():
    valid_proxy = find_valid_proxy(api)

    return valid_proxy


if __name__ == '__main__':
    main()
