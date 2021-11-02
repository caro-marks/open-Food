from django.core.management import BaseCommand
from foodData.models import Product
import httpx
import gzip
import json
import os


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        files = httpx.get(
            'https://challenges.coode.sh/food/data/json/index.txt').text.split('\n')[:-1]
        main_path = f'https://challenges.coode.sh/food/data/json'
        timeout = httpx.Timeout(10.0, connect=60.0)
        for file in files:
            print(file)
            client = httpx.Client(timeout=timeout)
            with client.stream('GET', f'{main_path}/{file}') as data:
                with open(file, 'wb') as target:
                    for chunk in data.iter_raw(1024):
                        if chunk:
                            target.write(chunk)
            client.close()
            with gzip.open(file) as products:
                total_uploaded_products = 0
                for compressed_product in products:
                    print(total_uploaded_products)
                    product = json.loads(compressed_product.decode('utf-8'))
                    try:
                        obj, created = Product.objects.get_or_create(
                            code=product["code"] if "code" in product else None,
                            url=product["url"] if "url" in product else None,
                            creator=product["creator"] if "creator" in product else None,
                            created_t=product["created_t"] if "created_t" in product else None,
                            last_modified_t=product["last_modified_t"]if "last_modified_t" in product else None,
                            product_name=product["product_name"] if "product_name" in product else None,
                            generic_name=product["generic_name"] if "generic_name" in product else None,
                            quantity=product["quantity"] if "quantity" in product else None,
                            status='published'
                        )
                    except Exception as err:
                        raise Exception(err)
                    else:
                        total_uploaded_products += 1
                    finally:
                        if total_uploaded_products >= 100:
                            print(file, 'ended\n')
                            break
            os.remove(file)
