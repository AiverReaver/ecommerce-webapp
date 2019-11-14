from rest_framework_nested import routers
from apps.users.viewsets import SellerViewSet, CustomerViewSet
from apps.products.viewsets import ProductCategoryViewSet, ProductViewSet
from apps.carts.viewsets import CartViewSet
from apps.orders.viewsets import OrderViewSet

router = routers.DefaultRouter()

router.register("customers", CustomerViewSet)
router.register("sellers", SellerViewSet)
router.register("categories", ProductCategoryViewSet, base_name="categories")
router.register("cart", CartViewSet)

user_router = routers.NestedDefaultRouter(router, "customers", lookup="user")
category_router = routers.NestedDefaultRouter(router, "categories", lookup="category")

user_router.register("orders", OrderViewSet, base_name="orders")
category_router.register("products", ProductViewSet, base_name="products")

