"""

Portfolio: Arcanoid Game
#100DaysOfCode with Python
Day: 95
Date: 2023-08-02
Author: MC

"""

import requests
import pandas as pd
import matplotlib.pyplot as plt


# main urls
usd_url = 'usd'
chf_url = 'chf'
chf_eur = 'eur'


def get_data_from_NBP_API(currency):
    # main urls
    main_url = 'https://api.nbp.pl/api/exchangerates/rates/a/'
    left_url = '/last/100/?format=json'

    response = requests.get(main_url + currency + left_url)
    response.raise_for_status()

    return response.json()


print(get_data_from_NBP_API(usd_url))


