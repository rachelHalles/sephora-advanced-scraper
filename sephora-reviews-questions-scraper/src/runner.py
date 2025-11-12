thonimport json
import os
from extractors.sephora_product_parser import SephoraProductParser
from outputs.data_exporter import DataExporter

class SephoraScraper:
    def __init__(self, input_file, output_file):
        self.input_file = input_file
        self.output_file = output_file
        self.parser = SephoraProductParser()
        self.exporter = DataExporter()

    def run(self):
        with open(self.input_file, 'r') as file:
            products = json.load(file)
        extracted_data = []
        for product in products:
            product_data = self.parser.parse_product(product)
            extracted_data.append(product_data)
        self.exporter.export_data(self.output_file, extracted_data)

if __name__ == "__main__":
    scraper = SephoraScraper("data/inputs.sample.json", "data/sample_output.json")
    scraper.run()