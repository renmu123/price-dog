import json

import httpx
from lxml import etree


class Suruga:
    name = "suruga"

    def __init__(self):
        self.base_url = "https://www.suruga-ya.jp/product/detail"

    def parse(self, goods_id: str):
        return self._parse(goods_id)

    def get_response(self, goods_id: str):
        headers = {
        }
        url = f"{self.base_url}/{goods_id}"
        r = httpx.get(url, headers=headers, verify=False)
        return r

    def _parse(self, goods_id: str):
        r = self.get_response(goods_id)
        root = etree.HTML(r.content)
        el = root.xpath("//script[@type='application/ld+json']")[1]
        data = json.loads(el.text)

        return {
            "name": "qqq",
            "price": "qqq"
        }
