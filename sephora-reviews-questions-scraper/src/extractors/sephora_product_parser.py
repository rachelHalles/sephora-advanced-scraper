thonimport requests
from bs4 import BeautifulSoup

class SephoraProductParser:
    def __init__(self):
        self.base_url = "https://www.sephora.com"

    def parse_product(self, product_url):
        product_data = {
            "info": self.get_product_info(product_url),
            "product_variants": self.get_product_variants(product_url),
            "statistics": self.get_product_statistics(product_url),
            "reviews": self.get_product_reviews(product_url),
            "questions": self.get_product_questions(product_url)
        }
        return product_data

    def get_product_info(self, url):
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        name = soup.find("h1", {"class": "css-0"}).get_text()
        description = soup.find("span", {"class": "css-0"}).get_text()
        price = soup.find("span", {"class": "css-0"}).get_text()
        brand = soup.find("span", {"class": "css-0"}).get_text()
        return {
            "name": name,
            "description": description,
            "price": price,
            "brand": brand
        }

    def get_product_variants(self, url):
        return []

    def get_product_statistics(self, url):
        return {}

    def get_product_reviews(self, url):
        return []

    def get_product_questions(self, url):
        return []