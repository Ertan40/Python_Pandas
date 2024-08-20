from sqlalchemy import create_engine, Column, Integer, String, DECIMAL
from sqlalchemy.orm import declarative_base, sessionmaker

# Create a SQLite database
Base = declarative_base()
# Create a base class for declarative models
engine = create_engine('sqlite:///shop2.db', echo=True)


# Define the Item model
class Item(Base):
    __tablename__ = 'items'

    item_id = Column(Integer, primary_key=True)
    item_name = Column(String, nullable=False)
    item_price = Column(DECIMAL(10,2), nullable=False)
    item_quantity = Column(Integer, nullable=False)


# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()


def update_item_quantity(item_name, new_quantity):
    item = session.query(Item).filter_by(item_name=item_name).first()
    if item:
        item.item_quantity = new_quantity
        session.commit()
        print(f"Quantity for item '{item_name}' updated to {new_quantity}")
    else:
        print(f"Item {item_name} not found!")


item_name = 'Pizza'
new_quantity = '150'
update_item_quantity(item_name, new_quantity)
# Close the session
session.close()