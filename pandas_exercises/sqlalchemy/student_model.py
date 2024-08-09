## Write a Python program to create a SQLAlchemy model 'Student' with fields: 'id', 'studentname', and 'email'.

from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm import declarative_base, sessionmaker

# Create a base class for declarative models
Base = declarative_base()

# Create a SQLite in-memory database
engine = create_engine('sqlite:///demodatabase')


class Student(Base):
    __tablename__ = 'Students'

    id = Column(Integer, primary_key=True, autoincrement=True)
    studentname = Column(String, nullable=False)
    email = Column(String, nullable=False)

    def __repr__(self):
        return f"Student(id={self.id}, studentname={self.studentname}, email={self.email})"


# Create the table in the database
Base.metadata.create_all(engine)
# Create a session to interact with the database
Session = sessionmaker(bind=engine)
session = Session()

# Add a new Student to the database
new_student = Student(id=24, studentname='Liv Tyler', email='loveliv@gmail.com')
# To handle the IntegrityError exception and avoid the error, use a try-except block
try:
    session.add(new_student)
    session.commit()
    print('Student added successfully!')
except IntegrityError:
    print("A student with the same ID already exists. No new student added.")
    session.rollback()

# Query and print all Students from the database
result = session.query(Student).all()

for student in result:
    print(student.id, student.studentname, student.email)

# Close the session
session.close()

