import requests


def query(_ip):
    _url = 'http://ip-api.com/json/' + _ip
    _req = requests.get(_url).json()

    return '-'.join([_req.get('country'), _req.get('city'), _req.get('as')])


if __name__ == '__main__':
    print(query('222.65.110.95'))
