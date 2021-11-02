from django.core.management import BaseCommand
from foodData.models import Product
import httpx


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        page_size = 100
        fields = ''.join(['code', 'url', 'creator', 'created_t',
                         'last_modified_t', 'product_name', 'generic_name', 'quantity'])
        main_path = f"https://world.openfoodfacts.org/api/v2/search?json=true&page_size={page_size}&fields={fields}"
        data_fetch = True
        page = 5000
        timeout = httpx.Timeout(10.0, connect=60.0)
        client = httpx.Client(timeout=timeout)
        while data_fetch:
            products = client.get(main_path, params={"page": page}).json()
            if products["page_count"] is None:
                data_fetch = False
                client.close()
            else:
                print(page)
                for product in products["products"]:
                    try:
                        obj, created = Product.objects.get_or_create(
                            code=product["code"] if "code" in product else None,
                            url=product["url"] if "url" in product else None,
                            creator=product["creator"]
                            if "creator" in product
                            else None,
                            created_t=product["created_t"]
                            if "created_t" in product
                            else None,
                            last_modified_t=product["last_modified_t"]
                            if "last_modified_t" in product
                            else None,
                            product_name=product["product_name"]
                            if "product_name" in product
                            else None,
                            generic_name=product["generic_name"]
                            if "generic_name" in product
                            else None,
                            quantity=product["quantity"]
                            if "quantity" in product
                            else None,
                        )
                    except Exception as err:
                        raise Exception(err)
                page += 1
