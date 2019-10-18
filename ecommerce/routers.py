from rest_framework_nested import routers
from apps.products.viewsets import ProductCategoryViewSet, ProductViewSet
from apps.carts.viewsets import CartViewSet

router = routers.DefaultRouter()

router.register("categories", ProductCategoryViewSet, base_name="categories")
router.register("cart", CartViewSet)

category_router = routers.NestedDefaultRouter(router, "categories", lookup="category")

category_router.register("products", ProductViewSet, base_name="products")

