# 12. Write a Python program to list the top 2 products by sales quantity from the 'orders' table using the
# SQLAlchemy model.

from sqlalchemy import create_engine, Column, String, Integer, DECIMAL, ForeignKey, func
from sqlalchemy.orm import declarative_base, sessionmaker, relationship

Base = declarative_base()

engine = create_engine('sqlite:///shop2.db', echo=False)


class User(Base):
    __tablename__ = 'users'

    user_id = Column(Integer, primary_key=True)
    user_name = Column(String, nullable=False)
    user_mail = Column(String, nullable=False)


class Item(Base):
    __tablename__ = 'items'

    item_id = Column(Integer, primary_key=True)
    item_name = Column(String, nullable=False)
    item_price = Column(DECIMAL(10, 2), nullable=False)
    item_quantity = Column(Integer, nullable=False)
    orders = relationship('Order', back_populates='item')


class Order(Base):
    __tablename__ = 'orders'

    order_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    item_id = Column(Integer, ForeignKey('items.item_id'), nullable=False)
    order_quantity = Column(Integer, nullable=False)
    item = relationship("Item", back_populates="orders")


Session = sessionmaker(bind=engine)
session = Session()


def get_top_items_by_sales_quantity(top_n=2):
    # Query the top N products by sales quantity
    query = (session.query(Order.item_id, func.sum(Order.order_quantity).label('total_quantity'))
             .group_by(Order.item_id)
             .order_by(func.sum(Order.order_quantity).desc())
             .limit(top_n)
             )
    results = query.all()
    # Create a dictionary to store item_id -> total_quantity mapping
    product_quantity = dict(results)
    top_products = session.query(Item).filter(Item.item_id.in_(product_quantity.keys())).all()
    print(f"Top {top_n} items by sales quantity:")

    for product in top_products:
        quantity = product_quantity[product.item_id]
        print(f"Item: {product.item_name}, Sales Quantity: {quantity}")

        
# List the top 2 products by sales quantity
get_top_items_by_sales_quantity(top_n=2)
# Close the session
session.close()
