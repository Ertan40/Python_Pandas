# 5. Write a Python program that deletes a student from the 'students' table by their id.

from sqlalchemy import create_engine, Column, String, Integer
from sqlalchemy.orm import declarative_base, sessionmaker

# Create a base class for declarative models
Base = declarative_base()
# Create a SQLite in-memory database
engine = create_engine('sqlite:///demodatabase', echo=False)


class Student(Base):
    __tablename__ = 'students'
    id = Column(Integer, primary_key=True)
    studentname = Column(String, nullable=False)
    email = Column(String, nullable=False)


# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()


# Delete a student from the students table by their ID with below function
def delete_student_by_id(student_id):
    current_student = session.query(Student).filter_by(id=student_id).first()
    if current_student:
        session.delete(current_student)
        session.commit()
        print("Student deleted successfully!")
    else:
        print(f"Student with ID={student_id} not found")


# Call the delete_student_by_id function to delete a student
student_id = 10
delete_student_by_id(student_id)

# Close the session
session.close()