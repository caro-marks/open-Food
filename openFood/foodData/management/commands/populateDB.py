from django.core.management import BaseCommand
from foodData.models import Product
import httpx


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
        main_path = "https://world.openfoodfacts.org?json=true&page_size=100"
        data_fetch = True
        page = 1
        timeout = httpx.Timeout(10.0, connect=60.0)
        client = httpx.Client(timeout=timeout)
        while data_fetch:
            products = client.get(main_path, params={"page": page}).json()
            if products["page_count"] is None:
                data_fetch = False
                client.close()
            else:
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
