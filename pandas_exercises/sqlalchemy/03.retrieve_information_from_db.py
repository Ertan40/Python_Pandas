## Write a Python program that retrieves a student's information from the `students` table using their id.

from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import declarative_base, sessionmaker

# Create a base class for declarative models
Base = declarative_base()
# Connect to the database
engine = create_engine('sqlite:///demodatabase')


class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    studentname = Column(String, nullable=False)
    email = Column(String, nullable=False)


# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()


# Function to retrieve a student's information by ID
def get_student_by_id(student_id):
    student = session.query(Student).filter_by(id=student_id).first()
    if student:
        print(f"Student found: ID={student.id}, Name={student.studentname}, Email={student.email}")
    else:
        print(f"A student with the following ID={student_id} not found.")


def get_all_students():
    students = session.query(Student).all()
    if students:
        for student in students:
            print("List of students:")
            print(f"ID={student.id}, Name={student.studentname}, Email={student.email}")
    else:
        print("There are no students")


get_student_by_id(24)
get_student_by_id(2)
get_all_students()
# Close the session
session.close()