import os

import requests
from bs4 import BeautifulSoup


class MasadoraSuruga:
    def __init__(self):
        self.name = "masadoraSuruga"
        self.base_url = "https://surugaya.masadora.jp/product/detail"

    def parse(self, goods_id: str):
        return self._parse(goods_id)

    def _parse(self, goods_id: str):
        print(os.getenv("MASADORA_SURUGA_COOKIE"))
        headers = {
            "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/51.0.2704.103 Safari/537.36",
            "Referer": "https://surugaya.masadora.jp/search?category=&search_word=TAKAMICHI+SUMMER+WORKS&searchbox=1&is_marketplace=0",
            "Host": "surugaya.masadora.jp",
            "Cookie": os.getenv("MASADORA_SURUGA_COOKIE")
        }
        url = f"{self.base_url}/{goods_id}"
        r = requests.get(url, headers=headers)
        soup = BeautifulSoup(r.text, 'html.parser')
        item_title = soup.find('h1', id='item_title').get_text()
        price = soup.find_all('span', color='orange')[0].get_text()

        return {
            "name": item_title,
            "price": price
        }
