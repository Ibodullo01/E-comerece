import csv
import pandas as pd
from django.core.management.base import BaseCommand
from product.models import Product

class Command(BaseCommand):
    help = 'Import products from a CSV or Excel file'

    file_path = "/product/management/"

    def add_arguments(self, parser):
        parser.add_argument('file_path', type=str, help='The path to the CSV or Excel file')

    def handle(self, *args, **kwargs):
        file_path = kwargs['file_path']
        print(file_path)
        if file_path.endswith('.csv'):
            self.import_csv(file_path)
        elif file_path.endswith('.xlsx'):
            self.import_excel(file_path)
        else:
            self.stdout.write(self.style.ERROR('Siz csv yoki excell formatidagi fayl topilmadi ! '))

    def import_csv(self, file_path):
        with open(file_path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            products = []
            for row in reader:
                products.append(Product(
                    title=row['title'],
                    price=row['price'][1:],
                    description=row.get('description', ''),
                    category_id=row['category_id'],
                    quantity=row['quantity'],
                    details=row['details']

                ))
            Product.objects.bulk_create(products)
            self.stdout.write(self.style.SUCCESS(f'Successfully imported {len(products)} products'))

    def import_excel(self, file_path):
        df = pd.read_excel(file_path)
        products = []
        for index, row in df.iterrows():
            products.append(Product(
                name=row['name'],
                price=row['price'],
                description=row.get('description', '')
            ))
        Product.objects.bulk_create(products)
        self.stdout.write(self.style.SUCCESS(f'Successfully imported {len(products)} products'))
