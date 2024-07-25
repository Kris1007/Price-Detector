import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

URL = "YOUR AMAZON LINK"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/126.0.0.0 Safari/537.36 Edg/126.0.0.0",
    "Accept-Language": "en-US,en;q=0.9,en-IN;q=0.8",
}

response = requests.get(URL, headers)
webpage = response.text

soup = BeautifulSoup(webpage, "lxml")
price = soup.select_one(selector="span .a-offscreen").getText()
price_without_dollar = price[1:]
price_without_dollar = float(price_without_dollar)
print(price_without_dollar)

# My microsoft Id app password
MY_EMAIL = "ENTER THE EMAIL YOU WANT TO USE"
MY_PASSWORD = "YOUR APP PASSWORD"
USER_EMAIL = "ENTER THE USER EMAILS"

PRICE_TO_BUY = 55  # Enter the amount you want to enter

if price_without_dollar <= PRICE_TO_BUY:
    with smtplib.SMTP("smtp.office365.com") as connection: # you can use "smtp.gmail.com" if you have a gmail account or "smtp.mail.yahoo.com" if you have a yahoo account
        connection.starttls()
        connection.login(user=MY_EMAIL, password=MY_PASSWORD)
        connection.sendmail(from_addr=MY_EMAIL, to_addrs=USER_EMAIL, msg=f"Subject:DISCOUNT!\n\nThe price of your cricket bat is ${price_without_dollar}.\nOrder it online on {URL}  :)")

