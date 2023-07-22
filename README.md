## Token Scraper using Python

![Python](https://img.shields.io/badge/python-v3.8%2B-blue)
![beautifulsoup4](https://img.shields.io/badge/beautifulsoup4-v4.9.3-brightgreen)

This is a simple Python web scraper that fetches data about the top 10 tokens from [CoinMarketCap](https://coinmarketcap.com/). The script utilizes the `beautifulsoup4` library for parsing the HTML content of the website and extracting the relevant information.

### Prerequisites

- Python 3.8 or higher installed on your system.
- Install the `beautifulsoup4` library using pip:

```bash
pip install beautifulsoup4
```

### Usage

1. Clone this repository:

```bash
git clone https://github.com/allyn8444/token-scraper.git
```

2. Navigate to the project directory:

```bash
cd token-scraper
```

3. Run the Python script:

```bash
python scraper.py
```

The script will fetch the current values of the top 10 tokens and display the output in the terminal.

### Documentation

You can find the official documentation for `beautifulsoup4` library [here](https://www.crummy.com/software/BeautifulSoup/bs4/doc/). It provides comprehensive details on how to use the library for parsing HTML and XML documents.

### Disclaimer

This project is intended for educational and informational purposes only. Please be aware that scraping websites without permission may violate their terms of service. Additionally, this script relies on the current structure of the CoinMarketCap website. If the website's source structure changes, the scraper may no longer function correctly. Use the scraper responsibly and in accordance with the website's guidelines.

**Note:** The data fetched by this scraper may not be real-time and is subject to change based on the website's data updates.

Feel free to use, modify, and distribute this code as per your requirements. Happy scraping! 🚀
