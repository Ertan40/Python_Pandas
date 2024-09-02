# # Write a Python program to retrieve all orders for a specific user from the 'Order' table user using the
# SQLAlchemy model.

from sqlalchemy import create_engine, Column, Integer, String, DECIMAL, ForeignKey
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
    item_price = Column(DECIMAL(10,2), nullable=False)
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


def get_orders_for_user(user_id):
    curr_orders = session.query(Order).filter_by(user_id=user_id).all()
    return curr_orders


user_id = 1
orders = get_orders_for_user(user_id)

print(f"Orders for user {user_id}:")
for order in orders:
    print(f"Order ID: {order.order_id}, Item ID: {order.item_id}, Quantity: {order.order_quantity}")


# Close the session
session.close()