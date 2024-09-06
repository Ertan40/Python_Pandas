# Write a Python program to delete an order from the 'Order' table by its id. Use the SQLAlchemy model.

from sqlalchemy import create_engine, Column, String, DECIMAL, Integer, ForeignKey
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
    orders = relationship('Order', back_populates='item')


class Order(Base):
    __tablename__ = 'orders'
    order_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.user_id'), nullable=False)
    item_id = Column(Integer, ForeignKey('items.item_id'), nullable=False)
    order_quantity = Column(Integer, nullable=False)
    item = relationship('Item', back_populates='orders')


# Create a session to interact with DB
Session = sessionmaker(bind=engine)
session = Session()


def delete_order_by_id(order_id):
    order = session.query(Order).filter_by(order_id=order_id).first()
    if order:
        session.delete(order)
        session.commit()
        print(f"Order with ID {order_id} deleted successfully!")
    else:
        print(f"Order with ID {order_id} not found.")


order_id_to_delete = 2

delete_order_by_id(order_id_to_delete)
# Close the session
session.close()








