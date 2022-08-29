### Description

The script shortens links with the service [bitly.com](https://bitly.com)

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

Set your token:
```
echo 'BITLY_TOKEN=<your token>' >> ./.env
```


### Run

Get the short link:
```
python ./main.py

Enter your url: http://llanfairpwllgwyngyllgogerychwyrndrobwllllantysiliogogogoch.co.uk

Your shorten url: https://bit.ly/3Th2ZnH
```


Get the number of clicks on your link:
```
python ./main.py

Enter your url: https://bit.ly/3Th2ZnH

Total clicks: 2
```


