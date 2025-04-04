from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from warehouse_management.infrastructure.orm import Base, ProductORM, OrderORM
from warehouse_management.domain.models import Product, Order

def test_product_orm():
    product=Product(id=1, name="test_product", quantity=10, price=100)
    product_orm=ProductORM(id=product.id, name=product.name, quantity=product.quantity, price=product.price)
    assert product_orm.id==product.id
    assert product_orm.name==product.name
    assert product_orm.quantity==product.quantity
    assert product_orm.price==product.price

def test_order_orm():
    product=Product(id=1, name="test_product", quantity=10, price=100)
    order=Order(id=1, products=[product])
    product_orm=ProductORM(id=product.id, name=product.name, quantity=product.quantity, price=product.price)
    order_orm=OrderORM(id=order.id, products=[product_orm])
    assert order_orm.id==order.id
    assert order_orm.products[0].id==product.id

def save_and_retrieve_product():
    engine=create_engine("sqlite://")
    Base.metadata.create_all(engine)
    Session=sessionmaker(bind=engine)
    session=Session()
    
    product=Product(id=1, name="test_product", quantity=10, price=100)
    product_orm=ProductORM(id=product.id, name=product.name, quantity=product.quantity, price=product.price)
    session.add(product_orm)
    session.commit()
    retrieved_product=session.query(ProductORM).filter_by(id=product.id).one()
    assert retrieved_product.id==product.id
    assert retrieved_product.name==product.name