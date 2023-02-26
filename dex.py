from requests import get
import time
import os

starttime = time.time()
BASE = 'https://api.dexscreener.com/latest/dex/pairs/'

bot_token = "MTA3OTQzNDg0MTczODcxNTE3Nw.GbA6Dl.DozZwNAOe-C6OCv_ypun_g77h0Q12pTPG66YJA"


def pair_url(chainid, pair_add):
    url = BASE + f"{chainid}/{pair_add}"

    return url


def prices(url):
    response = get(url)
    data = response.json()["pair"]
    # print(data)

    data2 = []

    name = data["baseToken"]["name"]
    price = data["priceUsd"] + "$"
    volume = data["volume"]
    volume = {key: int(value / 1000) for key, value in volume.items()}
    pchange = data["priceChange"]
    pchange = {key: float(value) for key, value in pchange.items()}

    # print information
    # print(name, "\n",
    #       "Price:", price, "\n",
    #       "Price change:", pchange, "\n",
    #       "Volume:", volume)

    init_m5 = pchange["h1"]
    print(init_m5)
    return(init_m5)

    # for dt in data:
    #     name = dt["name"]

    # print(name)
    # return name


chainid = "ethereum"
pair_add = "0x68d01EfdFbe5C0eeBE3b19B571B18Ae6D6EE16FC"

m5_0 = prices(pair_url(chainid, pair_add))
m5_1 = m5_0


while abs(m5_0) + 5 > abs(m5_1):
    m5_1 = prices(pair_url(chainid, pair_add))
    print(m5_1)
    time.sleep(30.0 - ((time.time() - starttime) % 30.0))

os.system('say "Sudo Sudo Sudo"')
