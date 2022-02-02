import smtplib
import requests
from bs4 import BeautifulSoup


def scrap():

    URL = 'https://www.worten.pt/gaming/acessorios-gaming-pc/mais-acessorios-gaming/oculos-de-realidade-virtual-hp-reverb-g2-controladores-7364668?gclid=Cj0KCQiA9OiPBhCOARIsAI0y71Cn90FXfVWbrHIk6CYEShw4uzE0x0BEoBivl4SqqqO1sfIJCINoWPYaAujmEALw_wcB'

    headers = {
    "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36'}

    page = requests.get(URL, headers=headers)

    css_soup = BeautifulSoup(page.content, 'html.parser')

    title = css_soup.find(
    "h1", class_="w-product__name iss-product-name").get_text()

    price = css_soup.find("span", class_="w-product-price__main").get_text()
    
    if price < 749:
        mail_sender()
    else:
        None    


def mail_sender():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('--- Email ---', '--- password ---')
    subject = 'price went down'
    body = 'https://www.worten.pt/gaming/acessorios-gaming-pc/mais-acessorios-gaming/oculos-de-realidade-virtual-hp-reverb-g2-controladores-7364668?gclid=Cj0KCQiA9OiPBhCOARIsAI0y71Cn90FXfVWbrHIk6CYEShw4uzE0x0BEoBivl4SqqqO1sfIJCINoWPYaAujmEALw_wcB'
    msg = f"Subject: {subject}\n\n{body}"

    server.sendmail(
        'makemywesite@gmail.com' ,
        ' --- Email To address ---' ,
        msg
    )   
    server.quit()


scrap()