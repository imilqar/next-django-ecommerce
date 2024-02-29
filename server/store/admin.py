from django.contrib import admin
from unfold.admin import ModelAdmin, TabularInline
from mptt.admin import DraggableMPTTAdmin

from django.contrib.auth.models import Group, User
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _

from .models import (
    Category,
    Product,
    ProductImage,
    ProductSpecification,
    ProductSpecificationValue,
    ProductType,
)

admin.site.unregister(Group)
admin.site.unregister(User)


@admin.register(Group)
class GroupAdmin(ModelAdmin):
    pass


@admin.register(User)
class UserAdmin(UserAdmin, ModelAdmin):
    pass


@admin.register(Category)
class CategoryAdmin(DraggableMPTTAdmin, ModelAdmin):
    list_display = ("indented_title", "slug", "is_active")
    list_display_links = None

    def _tree_context(self, request):
        opts = self.model._meta
        return {
            "storageName": f"tree_{opts.app_label}_{opts.model_name}_collapsed",
            "treeStructure": self._build_tree_structure(self.get_queryset(request)),
            "levelIndent": self.mptt_level_indent,
            "messages": {
                "before": _("move node before node"),
                "child": _("move node to child position"),
                "after": _("move node after node"),
            },
            "expandTreeByDefault": self.expand_tree_by_default,
        }


class ProductSpecificationInline(TabularInline):
    model = ProductSpecification


@admin.register(ProductType)
class ProductTypeAdmin(ModelAdmin):
    inlines = [ProductSpecificationInline]


class ProductImageInline(TabularInline):
    model = ProductImage


class ProductSpecificationValueInline(TabularInline):
    model = ProductSpecificationValue


@admin.register(Product)
class ProductAdmin(ModelAdmin):
    inlines = [ProductSpecificationValueInline, ProductImageInline]
