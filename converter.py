import requests

API_KEY = '5c90dfd1308bc2669ea4a597'
BASE_URL = 'https://v6.exchangerate-api.com/v6/' + API_KEY + '/latest/'

def is_valid_currency_code(currency_code):
    # Fetch the list of valid currency codes from the API
    response = requests.get(BASE_URL + 'USD')  # Use USD as the base currency
    data = response.json()

    if response.status_code == 200 and 'conversion_rates' in data:
        valid_currency_codes = list(data['conversion_rates'].keys())
        return currency_code in valid_currency_codes
    else:
        # Handle API request failure or invalid response
        return False

def convert_currency(from_currency, to_currency, amount):
    if not is_valid_currency_code(from_currency) or not is_valid_currency_code(to_currency):
        return 'Invalid currency code. Please enter a valid code.'

    # Fetch the exchange rates
    response = requests.get(BASE_URL + from_currency)
    data = response.json()

    if response.status_code == 200 and 'conversion_rates' in data:
        conversion_rates = data['conversion_rates']

        if to_currency in conversion_rates:
            exchange_rate = conversion_rates[to_currency]
            converted_amount = amount * exchange_rate
            return f'{to_currency} {converted_amount:.2f}'
        else:
            return f'Conversion rate for {to_currency} not available.'
    else:
        return 'Failed to fetch exchange rates. Please try again later.'

# Optional: You might want to cache exchange rates to avoid unnecessary API calls.
# Implement a function to fetch and cache rates, and use it in convert_currency.
