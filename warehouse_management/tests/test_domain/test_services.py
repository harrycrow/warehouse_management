from unittest.mock import Mock
from warehouse_management.domain.models import Product, Order
from warehouse_management.domain.services import WarehouseService

def test_create_product():
    product_repo=Mock()
    order_repo=Mock()
    warehouse_service=WarehouseService(product_repo, order_repo)
    product=warehouse_service.create_product("test_product", 10, 100)
    product_repo.add.assert_called_once_with(product)

def test_create_order():
    product_repo=Mock()
    order_repo=Mock()
    warehouse_service=WarehouseService(product_repo, order_repo)
    product=Product(id=1, name="test_product", quantity=10, price=100)
    order=warehouse_service.create_order([product])
    order_repo.add.assert_called_once_with(order)