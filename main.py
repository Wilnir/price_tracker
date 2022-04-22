from bs4 import BeautifulSoup
import requests
import smtplib

user_agent = ""
accept_language = ""

response = requests.get("https://www.amazon.com/Instant-Pot-Duo-Evo-Plus/dp/B07W55DDFB/ref=sr_1_1?qid=1597662463"
                        , headers={"Accept-Language": accept_language, "User-Agent": user_agent})
soup = BeautifulSoup(response.content, "html.parser")
soup.prettify()
price = soup.find(name="span", class_="olpWrapper").get_text()
float_price = float(price.split("$")[1])
print(float_price)

MY_EMAIL = "xxxxxxxxx@yahoo.com"
PASSWORD = "*********"

if float_price < 250:
    connection = smtplib.SMTP("smtp.mail.yahoo.com", 587)
    connection.starttls()
    connection.login(MY_EMAIL, PASSWORD)
    connection.sendmail(
        from_addr=MY_EMAIL,
        to_addrs=MY_EMAIL,
        msg="Subject: PRICE DOWN\n\n"
    )
