from django.db import models
from django.utils.translation import gettext_lazy as _


class Product(models.Model):
    class StatusProduct(models.TextChoices):
        DRAFT = "DR", _("draft")
        TRASH = "TR", _("trash")
        PUBLISHED = "PB", _("published")

    status = models.CharField(max_length=2, choices=StatusProduct.choices)
    imported_t = models.DateTimeField(auto_now_add=True)

    code = models.TextField(default=None, null=True, db_index=True)
    url = models.TextField(default=None, null=True)
    creator = models.TextField(default=None, null=True)
    created_t = models.IntegerField(default=None, null=True)
    last_modified_t = models.IntegerField(default=None, null=True)
    product_name = models.TextField(default=None, null=True)
    generic_name = models.TextField(default=None, null=True)
    quantity = models.TextField(default=None, null=True)
