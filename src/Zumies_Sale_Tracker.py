import requests
from bs4 import BeautifulSoup
import time
import smtplib
from email.message import EmailMessage
import os


def main():
    product_identifier = input(
        "What is the name of the product you are looking for: ")
    sku = input("What is the product SKU: ")
    url = input("Enter the sales page you would like monitored: ")
    receiver = input(
        "What email do you want to be alerted on when a product is found: ")

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) ' +
        'AppleWebKit/537.36 (KHTML, like Gecko) ' +
        'Chrome/39.0.2171.95 Safari/537.36'}
    response = requests.get(url, headers=headers).text
    soup = BeautifulSoup(response, 'html.parser')
    analyzeData(soup, product_identifier, receiver, sku)


def analyzeData(soup, product_identifier, receiver, sku):
    found = False

    while not found:
        if str(soup).find(sku) > -1:
            email(receiver, product_identifier)
            found = True
        else:
            time.sleep(600)
            continue


def email(receiver, product_identifier):

    sender = 'ahmedbot@salestracker.com'
    msg = EmailMessage()

    msg.set_content("Zumies Sale Tracker here with some good news! " +
                    product_identifier + " is now on the sales page. Get it ASAP!")

    msg['Subject'] = 'Sale Update: ' + product_identifier + " Now on Sale!"
    msg['From'] = sender
    msg['To'] = receiver

    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(os.environ.get('EMAIL'), os.environ.get('PASSWORD'))
    server.send_message(msg)
    server.quit()


if __name__ == "__main__":
    main()
