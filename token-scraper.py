import requests
from bs4 import BeautifulSoup

url = "https://coinmarketcap.com/"
r = requests.get(url)
soup = BeautifulSoup(r.content, 'html.parser')

# Find the elements that contain the names of the crypto tokens and their values.
tokens = soup.find_all('a', class_='cmc-link')

# Flag to indicate if we should print tokens with "$"
should_print = False
counter = 0
current_token = ''
values = {}

# Iterate through the list of elements and store the values for each token.
desired_cryptos = ['BitcoinBTC', 'EthereumETH', 'TetherUSDT', 'XRPXRP', 'BNBBNB', 'USD CoinUSDC', 'SolanaSOL', 'CardanoADA', 'DogecoinDOGE', 'PolygonMATIC']
for token in tokens:
    string = str(token.text)
    if string in desired_cryptos:
        should_print = True
        current_token = string
        values[current_token] = []
    elif should_print and "$" in string:
        counter += 1
        values[current_token].append(string)
        if counter == 2:
            print(current_token)
            print(f"current price:  {values[current_token][0]}")
            print(f"volume (24):  {values[current_token][1]}")
            print("-"*10)
            counter = 0
            should_print = False
