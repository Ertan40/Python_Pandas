# 4. Write a Python program that updates a student's email in the 'students' table based on their id.

from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import declarative_base, sessionmaker
from sqlalchemy.exc import IntegrityError

engine = create_engine('sqlite:///demodatabase', echo=False)

Base = declarative_base()


class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    studentname = Column(String, nullable=False)
    email = Column(String, nullable=False)


# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()


def add_students(student_id, studentname, email):
    new_student = Student(id=student_id, studentname=studentname, email=email)
    try:
        session.add(new_student)
        session.commit()
        print("New student added successfully!")
    except IntegrityError:
        print(f"A student with the same ID {id} already exists. No new student added.")
        session.rollback()


# Let's add more students in db
students_to_add = [
    (1, "John Doe", "john@example.com"),
    (2, "Jane Smith", "jane@example.com"),
    (3, "Bob Johnson", "bob@example.com"),
    (4, "Alice Brown", "alice@example.com"),
    (5, "Charlie Davis", "charlie@example.com"),
    (6, "Diana Evans", "diana@example.com"),
    (7, "Edward Foster", "edward@example.com"),
    (8, "Fiona Green", "fiona@example.com"),
    (9, "George Harris", "george@example.com"),
    (10, "Hannah Irwin", "hannah@example.com")
]

for student in students_to_add:
    add_students(*student)


def update_student_mail(student_id, new_email):
    student = session.query(Student).filter_by(id=student_id).first()
    if student:
        student.email = new_email
        session.commit()
        print(f"Student email updated successfully")
    else:
        print(f"A student with the following ID={student_id} not found.")


# Update a user's email based on their ID
student_id = 2
new_email = 'jane@gmail.com'
update_student_mail(student_id, new_email)

# Close the session
session.close()