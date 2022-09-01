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

