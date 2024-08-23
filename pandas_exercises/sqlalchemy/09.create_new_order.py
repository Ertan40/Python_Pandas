from sqlalchemy import create_engine, Column, Integer
from sqlalchemy.orm import declarative_base, sessionmaker


Base = declarative_base()

engine = create_engine('sqlite:///shop2.db', echo=True)


class Order(Base):
    __tablename__ = 'orders'

    order_id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    item_id = Column(Integer, nullable=False)
    order_quantity = Column(Integer, nullable=False)


# Create session
Session = sessionmaker(bind=engine)
session = Session()


def create_order(user_id, item_id, order_quantity):
    new_order = Order(order_id=103, user_id=user_id, item_id=item_id, order_quantity=order_quantity)
    session.add(new_order)
    session.commit()
    print("New order created successfully")


# Create a new order
user_id = 1
item_id = 1
order_quantity = 4
create_order(user_id, item_id, order_quantity)
session.close()