## 2. Write a Python program that adds a new student to the 'students' table with a given id, studentname and email.

from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import declarative_base, sessionmaker

# Create a base class for declarative models
Base = declarative_base()
# Create a SQLite in-memory database
engine = create_engine('sqlite:///students.db')


class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    studentname = Column(String, nullable=False)
    email = Column(String, nullable=False)


# Create the table in the database if it doesn't exist
Base.metadata.create_all(engine)
# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()


# Add a new student to the database
def add_student(id, studentname, email):
    new_student = Student(id=id, studentname=studentname, email=email)
    try:
        session.add(new_student)
        session.commit()
        print("New student added successfully!")
    except IntegrityError:
        print(f"A student with the same ID {id} already exists. No new student added.")
        session.rollback()


# Call the add_student function to add a new student
add_student(2, 'Jenny Block', 'jblock@test.com')
# Close the session
session.close()

## In case you want to add more than 1 student
# students_to_add = [
#     (1, "John Doe", "john@example.com"),
#     (2, "Jane Smith", "jane@example.com"),
#     (3, "Bob Johnson", "bob@example.com"),
#     (4, "Alice Brown", "alice@example.com"),
#     (5, "Charlie Davis", "charlie@example.com"),
#     (6, "Diana Evans", "diana@example.com"),
#     (7, "Edward Foster", "edward@example.com"),
#     (8, "Fiona Green", "fiona@example.com"),
#     (9, "George Harris", "george@example.com"),
#     (10, "Hannah Irwin", "hannah@example.com")
# ]
# # Add all students
# for student in students_to_add:
#     add_student(*student)
# # Close the session
# session.close()