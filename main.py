import requests
import lxml
from bs4 import BeautifulSoup
import smtplib

url = "https://www.amazon.in/Sennheiser-HD-599-Open-Back-Headphones/dp/B01L1IICR2/ref=sr_1_3?dchild=1&keywords=SENNHEISER+HD+599+Open+Back+Headphone%2C+Ivory+%28B01L1IICR2%29&qid=1626322419&sr=8-3"

header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36 Edg/91.0.864.67",
    "Accept-Language": "en-US,en;q=0.9",
}

response = requests.get(url, headers = header)

soup = BeautifulSoup(response.content, "lxml")

price = soup.find(id="priceblock_ourprice").getText()

price_num = price.split("₹")[1]

prices = price_num.split(',')

price_str = ""
for pri in prices:
    price_str += pri
price_float = float(price_str)

print(price_float)

title_of_product = soup.find(id="productTitle").getText().strip()

print(title_of_product)

BUY_PRICE = 17000

if BUY_PRICE > price_float:

    message = f"{title_of_product} is now at {price_float} \n"

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(user="tesingtester02@gmail.com", password="ponnu@123")
        connection.sendmail(from_addr="tesingtester02@gmail.com", to_addrs="ponnulings@gmail.com",
                            msg=f"Subject:Amazon Price Alert ! \n\n {message} \n url = {url} \n"
                                f"Buy now !!".encode("UTF-8"))