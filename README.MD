### Description

Скрипт сокращает ссылки при помощи сервиса [bitly.com](https://bitly.com)

### Install

```
git clone https://github.com/RNDpacman/shorten_url.git
```

```
python -m venv ./shorten_url
```

```
cd ./shorten_url
```

```
source ./bin/activate
```

```
pip install --upgrade pip
```

```
pip install -r requirements.txt
```


### Run

```
export BITLY_TOKEN=<your token>
```


Get the short link:
```
python ./main.py http://llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch.co.uk

Your shorten url: https://bit.ly/3Th2ZnH
```


Get the number of clicks on your link:
```
python ./main.py https://bit.ly/3Th2ZnH
Total clicks: 1
```

### Help

```
python ./main.py --help
```

```
usage: main.py [-h] url

Get clicks bitlink or Shorten url

positional arguments:
  url         Long url or Bitlink

options:
  -h, --help  show this help message and exit
```

