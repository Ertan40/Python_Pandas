# # 7. Write a Python program to retrieve items with a price greater than a certain value from the 'items' table
# using the SQLAlchemy model.

from sqlalchemy import create_engine, Column, Integer, String, DECIMAL
from sqlalchemy.orm import sessionmaker, declarative_base

# Create a base class for declarative models
Base = declarative_base()
# Create a SQLite database named shop.db
engine = create_engine('sqlite:///shop2.db')
# To connect to PostgreSQL instead of SQLite:
# engine = create_engine('postgresql+psycopg2://username:password@host:port/database_name')
# engine = create_engine('postgresql+psycopg2://postgres-user:password@127.0.0.1:5432/sales_db')
# You can use Base.metadata.create_all(engine) to create the tables based on your models.


# Define the Item model
class Item(Base):
    __tablename__ = 'items'

    item_id = Column(Integer, primary_key=True)
    item_name = Column(String, nullable=False)
    item_price = Column(DECIMAL(10, 2), nullable=False)
    item_quantity = Column(Integer, nullable=False)


# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()


def find_items_with_price_above(threshold_price):
    items = session.query(Item).filter(Item.item_price > threshold_price).all()
    return items


threshold_price = 2
test_case = find_items_with_price_above(threshold_price)
print(f"Items with a price greater than {threshold_price}:")
for item in test_case:
    print(f" *Item ID: {item.item_id}, Name: {item.item_name}, Price: {item.item_price}")


# Close the session
session.close()