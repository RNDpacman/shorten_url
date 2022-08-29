import requests
import os
import argparse
from urllib.parse import urlparse
from dotenv import load_dotenv


def get_short(long_url: str, token) -> str:
    '''
    Возвращает сокращенную версию long_url
    '''
    api_url = 'https://api-ssl.bitly.com/v4/shorten'
    headers = {'Authorization': token}
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

def get_clicks(bitlink: str, token) -> int:
    '''
    Возвращает суммарное количество кликов для bitlink
    '''

    parsed_url = urlparse(bitlink)
    api_url = f'https://api-ssl.bitly.com/v4/bitlinks/{parsed_url.netloc}{parsed_url.path}/clicks/summary'
    headers = {'Authorization': token}
    clicks = requests.get(api_url, headers=headers)
    clicks.raise_for_status()

    return clicks.json()['total_clicks']


def is_bitlink(url: str, token) -> bool:
    '''
    Является ли url корректным bitlink
    '''

    headers = {'Authorization': token}
    parsed_url = urlparse(url)
    api_url = f'https://api-ssl.bitly.com/v4/bitlinks/{parsed_url.netloc}{parsed_url.path}'
    bitlink_info = requests.get(api_url, headers=headers)

    return bitlink_info.ok


def main():

    if load_dotenv():
        token = os.getenv('BITLY_TOKEN')
    else:
        raise Exception('You did not specify a token')

    args = get_parser()

    if is_bitlink(args.url, token=token):
        try:
            clicks = get_clicks(args.url, token=token)
        except requests.exceptions.HTTPError:
            print('Error: check url')
        else:
            print('Total clicks:', clicks)
    else:
        try:
            short_url = get_short(long_url=args.url, token=token)
        except requests.exceptions.HTTPError:
            print('Error: Check your url')
        else:
            print('Your shorten url:', short_url)


if __name__ == '__main__':
    main()
