from django.db import models
from django.urls import reverse
from django.utils.translation import gettext_lazy as _
from mptt.models import MPTTModel, TreeForeignKey


class Category(MPTTModel):
    name = models.CharField(
        verbose_name=_("Name"),
        help_text=_("Required and unique"),
        max_length=255,
        unique=True,
    )
    slug = models.SlugField(verbose_name=_("Slug"), max_length=255, unique=True)
    parent = TreeForeignKey(
        "self", on_delete=models.CASCADE, null=True, blank=True, related_name="children"
    )
    is_active = models.BooleanField(default=True)

    class MPTTMeta:
        order_insertion_by = ["name"]

    class Meta:
        verbose_name = _("Category")
        verbose_name_plural = _("Categories")

    def get_absolute_url(self):
        return reverse("store:category_list", args=[self.slug])

    def __str__(self):
        return self.name


class ProductType(models.Model):
    name = models.CharField(
        verbose_name=_("Name"),
        help_text=_("Required and unique"),
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=True)

    class Meta:
        verbose_name = _("Product Type")
        verbose_name_plural = _("Product Types")

    def __str__(self):
        return self.name


class ProductSpecification(models.Model):
    name = models.CharField(
        verbose_name=_("Name"), help_text=_("Required"), max_length=255
    )
    product_type = models.ForeignKey(ProductType, on_delete=models.RESTRICT)

    class Meta:
        verbose_name = _("Product Specification")
        verbose_name_plural = _("Product Specifications")

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(
        verbose_name=_("Name"), help_text=_("Required"), max_length=255
    )
    desc = models.TextField(verbose_name=_("Description"), blank=True)
    slug = models.SlugField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.RESTRICT)
    product_type = models.ForeignKey(ProductType, on_delete=models.RESTRICT)
    price = models.DecimalField(
        verbose_name=_("Price"),
        help_text=_("Maximum 999.99"),
        max_digits=5,
        decimal_places=2,
        error_messages={
            "name": {"max_length": _("The price must be between 0 and 999.99.")}
        },
    )
    discount_price = models.DecimalField(
        verbose_name=_("Discount price"),
        help_text=_("Maximum 999.99"),
        error_messages={
            "name": {
                "max_length": _("The price must be between 0 and 999.99."),
            },
        },
        max_digits=5,
        decimal_places=2,
    )
    is_active = models.BooleanField(
        verbose_name=_("Product visibility"),
        help_text=_("Change visibility"),
        default=True,
    )
    created_at = models.DateTimeField(
        _("Created at"), auto_now_add=True, editable=False
    )
    updated_at = models.DateTimeField(_("Updated at"), auto_now=True)

    class Meta:
        ordering = ("-created_at",)
        verbose_name = _("Product")
        verbose_name_plural = _("Products")

    def get_absolute_url(self):
        return reverse("store:product_detail", arg=[self.slug])

    def __str__(self):
        return self.name


class ProductSpecificationValue(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="product_specification_value"
    )
    specification = models.ForeignKey(ProductSpecification, on_delete=models.RESTRICT)
    value = models.CharField(
        verbose_name=_("Value"),
        help_text=_("Product specification value (maximum of 255 words"),
        max_length=255,
    )

    class Meta:
        verbose_name = _("Product Specification Value")
        verbose_name_plural = _("Product Specification Values")

    def __str__(self):
        return self.value


class ProductImage(models.Model):
    product = models.ForeignKey(
        Product, on_delete=models.CASCADE, related_name="product_image"
    )
    image = models.ImageField(
        verbose_name=_("Image"),
        help_text=_("Upload a product image"),
        upload_to="images/",
        default="images/default.png",
    )
    alt_text = models.CharField(
        verbose_name=_("Alternative text"), max_length=255, null=True, blank=True
    )
    is_feature = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True, editable=False)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name = _("Product Image")
        verbose_name_plural = _("Product Images")
