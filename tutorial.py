from bs4 import BeautifulSoup as bs
import requests

"""
TWITTER API KEYS AND STUFF
API key: 0bT8P7xI2ARoI56EoBM1GzIeT
API secret key: jtR1JyCLnAaIDcpwY1r8qpoVo7EaQMAtUfDZle0zvb49PIBgC7
Access token: 1272587244407328771-RcSEjhsOyvGXG2eaTZn0En0x39ZffX
Access token secret: AY6ROLZcCiJx8cj8cgiNgLftNF6lTy7vHJR5QS3gdT9Qt
"""

url = requests.get("https://dealsea.com/")

soup = bs(url.text, 'html.parser')

links = soup.find_all('a')

with open('output.txt', 'w') as f:
    for deal in links:
        try:
            if '/view-deal' in deal.get('href'):
                f.write(deal.string + '\n')        
        except:
            TypeError