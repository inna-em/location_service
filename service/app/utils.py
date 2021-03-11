from requests import get
from json import loads, dumps


def get_ip_data(ip: str):
    url = f"http://ipgeobase.ru:7020/geo?ip={ip}&json=1"
    result = get(url)
    result.encoding = 'windows-1251'
    return result.json()