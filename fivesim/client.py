import requests
import json
from fivesim.errors import *


class FiveSim:
    def __init__(self, api_key):
        self.__api_key = api_key
        self.__session = requests.Session()
        self.__auth_url: str = "https://5sim.net/v1/user/"
        self.__guest_url: str = "https://5sim.net/v1/guest/"
        self.__vendor_url: str = 'https://5sim.net/v1/vendor/'
        self.__session.headers = {
            "Authorization": "Bearer " + self.__api_key,
            "Accept": "application/json",
        }

    def __request(self, method, url):
        try:
            if method == "GET":
                resp = self.__session.get(url)
                if resp.status_code == 401:
                    raise ApiKeyInvalidError
                if resp.status_code == 400:
                    raise BadRequests(resp.text)
                if resp.text == 'no free phones':
                    raise NoPhoneNumberError('No number in stock')
                if resp.text == 'not enough user balance':
                    raise LowBalanceError('Not enough balance')
                try:
                    return json.loads(resp.text)
                except json.JSONDecodeError:
                    return resp.text
        except Exception as e:
            raise e

    def get_country_list(self) -> dict:
        return self.__request("GET", self.__guest_url + "countries")

    def product_requests(self, country: str, operator: str) -> dict:
        return self.__request("GET", self.__guest_url + 'products/' + country + '/' + operator)

    def price_requests(self) -> dict:
        return self.__request("GET", self.__guest_url + "prices")

    def price_requests_by_country(self, country: str) -> dict:
        return self.__request("GET", self.__guest_url + "prices?country=" + country)

    def price_requests_by_product(self, product: str) -> dict:
        return self.__request("GET", self.__guest_url + "prices?product=" + product)

    def price_requests_by_country_and_product(self, country: str, product: str) -> dict:
        return self.__request("GET", self.__guest_url + "prices?country=" + country + "&product=" + product)

    def get_balance(self) -> dict:
        return self.__request("GET", self.__auth_url + "profile")

    def buy_number(self, country: str, operator: str, product: str) -> dict:
        return self.__request("GET", self.__auth_url + "buy/activation/" + country + "/" + operator + "/" + product + '?ref=3b612d3c')

    def buy_hosting_number(self, country: str, operator: str, product: str) -> dict:
        return self.__request("GET", self.__auth_url + "buy/hosting/" + country + "/" + operator + "/" + product)

    def rebuy_number(self, product: str, number: str) -> dict:
        return self.__request("GET", self.__auth_url + "reuse/" + product + "/" + number)

    def check_order(self, order_id: str) -> dict:
        return self.__request("GET", self.__auth_url + "check/" + order_id)

    def finish_order(self, order_id: str) -> dict:
        return self.__request("GET", self.__auth_url + "finish/" + order_id)

    def cancel_order(self, order_id: str) -> dict:
        return self.__request("GET", self.__auth_url + "cancel/" + order_id)

    def ban_order(self, order_id: str) -> dict:
        return self.__request("GET", self.__auth_url + "ban/" + order_id)

    def sms_inbox_list(self, order_id: str) -> dict:
        return self.__request("GET", self.__auth_url + "sms/inbox/" + order_id)

    def btc_and_ltc_rates(self, currency: str) -> dict:
        return self.__request("GET", self.__auth_url + "payment/crypto/rates?currency=" + currency)

    def address_payment(self, currency: str) -> dict:
        return self.__request("GET", self.__auth_url + "payment/crypto/getaddress?currency=" + currency)

    def get_notifications(self, lang: str) -> dict:
        return self.__request("GET", self.__guest_url + "flash/" + lang)

    def vendor_statics(self) -> dict:
        return self.__request("GET", self.__auth_url + "vendor")

    def wallet_reverse(self) -> dict:
        return self.__request("GET", self.__vendor_url + "wallets")
