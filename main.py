#  curl 'https://demowebshop.tricentis.com/addproducttocart/catalog/31/1/1' \
#  -X 'POST' \
#  -H 'Accept: */*' \
#  -H 'Accept-Language: ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7' \
#  -H 'Connection: keep-alive' \
#  -H 'Content-Length: 0' \
#  -H 'Cookie: Nop.customer=f9fe8df4-b1f8-4b90-a9ee-ba11542eb344; ARRAffinity=92eb765899e80d8de4d490df907547e5cb10de899e8b754a4d5fa1a7122fad69; ARRAffinitySameSite=92eb765899e80d8de4d490df907547e5cb10de899e8b754a4d5fa1a7122fad69' \
#  -H 'Origin: https://demowebshop.tricentis.com' \
#  -H 'Referer: https://demowebshop.tricentis.com/' \
#  -H 'Sec-Fetch-Dest: empty' \
#  -H 'Sec-Fetch-Mode: cors' \
#  -H 'Sec-Fetch-Site: same-origin' \
#  -H 'User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/105.0.0.0 Safari/537.36' \
#  -H 'X-Requested-With: XMLHttpRequest' \
#  -H 'sec-ch-ua: "Google Chrome";v="105", "Not)A;Brand";v="8", "Chromium";v="105"' \
#  -H 'sec-ch-ua-mobile: ?0' \
#  -H 'sec-ch-ua-platform: "Windows"' \
#  -H 'sec-gpc: 1' \
#  --compressed

from uuid import uuid4
import requests


def test():
    print(uuid4())


def test_add_to_card_unauthorized():
    responce = requests.post(
        'https://demowebshop.tricentis.com/addproducttocart/catalog/31/1/1',
        cookies={'Nop.customer': 'f9fe8df4-b1f8-4b90-a9ee-ba11542eb344'})
    assert responce.status_code == 200
    assert responce.json()['success'] is True
    assert responce.json()['message'] == 'The product has been added to your <a href=\"/cart\">shopping cart</a>'


def test_add_to_cart_unauthorized_one_product():
    responce = requests.post(
        'https://demowebshop.tricentis.com/addproducttocart/catalog/31/1/1',
        cookies={'Nop.customer': str(uuid4())})
    assert responce.status_code == 200
    assert responce.json()['success'] is True
    assert responce.json()['message'] == 'The product has been added to your <a href=\"/cart\">shopping cart</a>'
    assert responce.json()['updatetopcartsectionhtml'] == '(1)'


'''
def test_add_to_cart_unauthorized_two_product():
    uid = str(uuid4())
    requests.post(
        'https://demowebshop.tricentis.com/addproducttocart/catalog/31/1/1',
        cookies={'Nop.customer': uid}
    )
    responce = requests.post(
        'https://demowebshop.tricentis.com/addproducttocart/catalog/31/1/1',
        cookies={'Nop.customer': uid}
    )

    assert responce.status_code == 200
    assert responce.json()['success'] is True
    assert responce.json()['message'] == 'The product has been added to your <a href=\"/cart\">shopping cart</a>'
    assert responce.json()['updatetopcartsectionhtml'] == '(2)
'''


def test_add_to_card_authorized():
    from dotenv import load_dotenv
    import os
    load_dotenv()
    login = os.getenv('user_login')
    password = os.getenv('user_password')
    responce = requests.post(
        'https://demowebshop.tricentis.com/login',
        data={'Email': login, 'Password': password}
    )
    auth_cookie = responce.cookies.get('NOPCOMMERCE.AUTH')
    print(auth_cookie)

