"""

Portfolio: Arcanoid Game
#100DaysOfCode with Python
Day: 95
Date: 2023-08-02
Author: MC

"""

import requests
import pandas as pd
import json
import matplotlib.pyplot as plt


# main urls
usd_url = 'usd'
chf_url = 'chf'
eur_url = 'eur'


def get_data_from_NBP_API(currency):
    # main urls
    main_url = 'https://api.nbp.pl/api/exchangerates/rates/a/'
    left_url = '/last/100/?format=json'

    response = requests.get(main_url + currency + left_url)
    response.raise_for_status()

    return response.json()


# get data from API
df_usd = pd.read_json(json.dumps(get_data_from_NBP_API(usd_url)['rates']))
df_chf = pd.read_json(json.dumps(get_data_from_NBP_API(chf_url)['rates']))
df_eur = pd.read_json(json.dumps(get_data_from_NBP_API(eur_url)['rates']))

# plot the results
ax = plt.gca()

parameters = {
    'kind': 'line',
    'x': 'effectiveDate',
    'y': 'mid',
    'ax': ax,
}

df_usd.plot(
    **parameters,
    label='USD',
    color='red'
)

df_chf.plot(
    **parameters,
    label='CHF',
    color='green'
)

df_eur.plot(
    **parameters,
    label='EUR',
    color='blue'
)

plt.show()

