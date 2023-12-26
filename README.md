# FiveSim

A simple Python API for <a href="https://5sim.net/">5sim.net</a>
#


## Installation

Before proceeding, you should register an account on [5sim.net](https://5sim.net/) and [generate a personal API key](https://5sim.net/settings/security) to use. 

Install from source:

``` bash
pip install git+https://github.com/scribesavant/5sim-python.git
```

Alternatively, install from [PyPI](https://pypi.org/project/5sim-python/):

```bash
pip install 5sim-python
```
<hr>

#### Client 

```python
from fivesim import FiveSim

# These example values won't work. You must get your own api_key
API_KEY = 'ey.............'

proxies = {
   'http': 'http://proxy.example.com:8080',
   'https': 'http://secureproxy.example.com:8090',
}

client = FiveSim(API_KEY, proxies) # Optional proxy 
```
#
### Endpoints
Official docs [here](https://docs.5sim.net/)
#### User

```python
# Balance request
client.get_balance() # Provides profile data: email, balance and rating.
```
#### Products and prices
```python

# Products request
client.product_requests(country='russia', product='telegram') # To receive the name, the price, quantity of all products, available to buy.

# Prices request
client.price_requests() # Returns product prices

# Prices by country
client.price_requests_by_country(country='russia') # Returns product prices by country

# Prices by product
client.price_requests_by_product(product='telegram') # Returns product prices by product

# Prices by country and product
client.price_requests_by_country_and_product(country='russia' ,product='telegram') # Returns product prices by country and specific product
```
#### Purchase

```python
# Buy activation number
client.buy_number(country='russia', operator='any', product='telegram') # Buy new activation number

# Buy hosting number
client.buy_hosting_number(country='russia', operator='any', product='amazon') # Buy new hosting number

# Re-buy number
client.rebuy_number(product='telegram', number='7485.....') # Re-buy number 
```
#### Order management
```python
# Check order (Get SMS)
client.check_order(order_id='12345678') # Check the sms was received

# Finish order
client.finish_order(order_id='12345678') # Finish the order after code received

# Cancel order
client.cancel_order(order_id='12345678') # Cancel the order

# Ban order 
client.ban_order(order_id='12345678') # Cancel the order if banned from the service

# SMS inbox list
client.sms_inbox_list(order_id='12345678') # Get SMS inbox list by order's id.
```

Powered by [ScribeSavant](https://github.com/scribesavant).