import requests
import os
import argparse
from urllib.parse import urlparse


TOKEN = os.getenv('BITLY_TOKEN')

def get_shorten(long_url: str) -> str:
    '''
    Возвращает сокращенную версию long_url
    '''
    api_url = 'https://api-ssl.bitly.com/v4/shorten'
    headers = {'Authorization': TOKEN}
    payload = {'long_url': long_url}
    shorten_url = requests.post(api_url, json=payload, headers=headers)
    shorten_url.raise_for_status()

    return shorten_url.json()['link']

def get_parser():
    '''
    Парсит параметры командной строки и возвращает объект парсера
    '''

    parser = argparse.ArgumentParser(description='Get clicks bitlink or Shorten url')
    parser.add_argument('url', help='Long url or Bitlink')

    return parser.parse_args()

def get_clicks(bitlink: str, unit='day', units='-1'):
    '''
    Возвращает суммарное количество кликов для bitlink
    '''

    parsed_url = urlparse(bitlink)
    api_url = f'https://api-ssl.bitly.com/v4/bitlinks/{parsed_url.netloc}{parsed_url.path}/clicks/summary'
    headers = {'Authorization': TOKEN}
    payload = {'unit': unit, 'units': units}
    clicks = requests.get(api_url, params=payload, headers=headers)
    clicks.raise_for_status()

    return clicks.json()['total_clicks']


def is_bitlink(url: str) -> bool:
    '''
    Является ли url корректным bitlink
    '''

    headers = {'Authorization': TOKEN}
    parsed_url = urlparse(url)
    api_url = f'https://api-ssl.bitly.com/v4/bitlinks/{parsed_url.netloc}{parsed_url.path}'
    bitlink_info = requests.get(api_url, headers=headers)

    try:
        bitlink_info.raise_for_status()
    except requests.exceptions.HTTPError:
        return False
    else:
        return True


def main():

    if not TOKEN:
        raise Exception('token is empty')

    args = get_parser()

    if is_bitlink(args.url):
        try:
            clicks = get_clicks(args.url)
        except requests.exceptions.HTTPError:
            print('Error: check url')
        else:
            print('Total clicks:', clicks)
    else:
        try:
            shorten_url = get_shorten(long_url=args.url)
        except requests.exceptions.HTTPError:
            print('Error: Check your url')
        else:
            print('Your shorten url:', shorten_url)


if __name__ == '__main__':
    main()
