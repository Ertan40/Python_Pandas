# # 11. Write a Python program to calculate and display the total cost of all orders for a given user using the
# SQLAlchemy model.

from sqlalchemy import create_engine, Column, Integer, String, DECIMAL, ForeignKey, func
from sqlalchemy.orm import sessionmaker, declarative_base, relationship

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
    orders = relationship("Order", back_populates="item")  # Define the relationship to Order


class Order(Base):
    __tablename__ = 'orders'

    order_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    item_id = Column(Integer, ForeignKey('items.item_id'), nullable=False)
    order_quantity = Column(Integer, nullable=False)
    item = relationship("Item", back_populates="orders")  # Define the relationship to Item


Session = sessionmaker(bind=engine)
session = Session()


def calculate_total_orders(user_id):
    total_cost = (session.query(func.sum(Order.order_quantity * Item.item_price))
                  .join(Item, Order.item_id == Item.item_id)
                  .filter(Order.user_id == user_id)
                  .scalar())
    return total_cost


user_id = 1
total_cost = calculate_total_orders(user_id=user_id)
print(f"Total cost of all orders for user {user_id}: {total_cost:.2f}$")
# Close the session
session.close()