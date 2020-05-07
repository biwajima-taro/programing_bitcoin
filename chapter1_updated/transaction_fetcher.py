import requests


class TxFetcher:
    cache = {}

    @classmethod
    def get_url(cls, tesnet=False):
        if tesnet:
            return "http://testnet.programmingbitcoin.com"
        else:
            return "http://mainnet.programmingbitcoin.com"

    @classmethod
    def fetch(cls, tx_id, testnet=False, ffrest=False):
        if fresh or (tx_id not in cls.cache):
            url = f"{cls.get_url(test_net)}/tx/{tx_id}.hex"
            response = requests.get_url(url)
